#!/usr/bin/env python3
import asyncio
import cowsay

clients = {}
registered = {}
me_cows = {}
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
                    text = ', '.join(list(registered.keys()))
                    send = asyncio.create_task(reader.readline())
                    await clients[me].put(f"{text}")
                elif cmd == 'cows':
                    text = ', '.join(cows)
                    send = asyncio.create_task(reader.readline())
                    await clients[me].put(f"{text}")
                elif cmd == 'quit':
                    del registered[me_cows[me]]
                    cows.append(me_cows[me])
                    del me_cows[me]
                    q = 1
                    break
                elif cmd.startswith('login '):
                    cow = cmd.split('login ')[1]
                    if cow in cows and cow not in list(registered.keys()):
                        cows.remove(cow)
                        registered[cow] = clients[me]
                        me_cows[me] = cow
                        send = asyncio.create_task(reader.readline())
                        await clients[me].put(f"Registered!")
                    else:
                        send = asyncio.create_task(reader.readline())
                        await clients[me].put(f"Incorrect cow name!")
                elif cmd.startswith('say ') and cmd.count(' ') >= 2:
                    text = cmd.split('say ')[1]
                    cow, msg = text[:text.index(' ')], text[text.index(' ') + 1:]
                    if clients[me] not in list(registered.values()):
                        send = asyncio.create_task(reader.readline())
                        await clients[me].put(f"You're not registered!")
                    elif cow not in list(registered.keys()):
                        send = asyncio.create_task(reader.readline())
                        await clients[me].put(f"{cow} is not registered!")
                    else:
                        send = asyncio.create_task(reader.readline())
                        await registered[cow].put(f"{msg}")
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
