#!/usr/bin/env python3
import asyncio
import cowsay

clients = {}
registered = []
cows = cowsay.list_cows()

async def chat(reader, writer):
    me = "{}:{}".format(*writer.get_extra_info('peername'))
    print(me)
    clients[me] = asyncio.Queue()
    send = asyncio.create_task(reader.readline())
    receive = asyncio.create_task(clients[me].get())
    q = 0
    while not reader.at_eof():
        done, pending = await asyncio.wait([send, receive], return_when=asyncio.FIRST_COMPLETED)
        for q in done:
            if q is send:
                cmd = q.result().decode()[:-1]
                print('1', cmd)
                if cmd == 'who':
                    text = ', '.join(registered)
                    send = asyncio.create_task(reader.readline())
                    for out in clients.values():
                        if out is clients[me]:
                            await out.put(f"{text}")
                elif cmd == 'cows':
                    text = ', '.join(cows)
                    send = asyncio.create_task(reader.readline())
                    for out in clients.values():
                        if out is clients[me]:
                            await out.put(f"{text}")
                elif cmd == 'quit':
                    q = 1
                    break
                else:
                    send = asyncio.create_task(reader.readline())
                    for out in clients.values():
                        if out is not clients[me]:
                            await out.put(f"{me} {q.result().decode().strip()}")
            elif q is receive:
                print('2', q.result())
                receive = asyncio.create_task(clients[me].get())
                writer.write(f"{q.result()}\n".encode())
                await writer.drain()
        if q == 1:
            break
    send.cancel()
    receive.cancel()
    print(me, "DONE")
    del clients[me]
    writer.close()
    await writer.wait_closed()

async def main():
    server = await asyncio.start_server(chat, '0.0.0.0', 1337)
    async with server:
        await server.serve_forever()

asyncio.run(main())
