#!/usr/bin/env python3
import cmd
import socket
import sys
import threading
import readline
from contextlib import contextmanager

class CowChatClient(cmd.Cmd):
    prompt = ""
    
    def __init__(self, host='localhost', port=1337):
        super().__init__()
        self.host = host
        self.port = port
        self.sock = None
        self.connected = False
        self.receive_thread = None
        self.running = True
        self.actual_cows = [0]
        self.actual_who = [0]
        
    def connect(self):
        """Connect to the server"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self.connected = True
            self.receive_thread = threading.Thread(target=self.receive_messages, daemon=True)
            self.receive_thread.start()
            return True
        except Exception as e:
            print(f"Failed to connect: {e}")
            return False
    
    def receive_messages(self):
        """Background thread to receive messages from server"""
        while self.running and self.connected:
            try:
                data = self.sock.recv(1024)
                if not data:
                    break
                message = data.decode().rstrip()
                if message.startswith('!!!'):
                    self.actual_cows = message[3:].split(',')
                elif message.startswith('###'):
                    self.actual_who = message[3:].split(',')
                else:
                    print(f"{message}")
                    print(f"{self.prompt}{readline.get_line_buffer()}", end="", flush=True)
            except:
                break
        self.connected = False
    
    def send_command(self, cmd):
        """Send command to server and wait for response"""
        if not self.connected:
            print("Not connected to server!")
            return None
        
        try:
            self.sock.sendall(f"{cmd}\n".encode())
        except Exception as e:
            print(f"Error sending command: {e}")
            self.connected = False
            return None
    
    def get_cows_list(self):
        """Get list of available cows from server"""
        response = self.send_command("get_cows")
        self.actual_cows = [0]
        while self.actual_cows == [0]:
            pass
        return self.actual_cows
    
    def get_who_list(self):
        """Get list of registered users from server"""
        response = self.send_command("get_who")
        self.actual_who = [0]
        while self.actual_who == [0]:
            pass
        return self.actual_who
    
    def do_login(self, arg):
        """Login with a cow name: login <cow_name>"""
        if not arg:
            return
        
        response = self.send_command(f"login {arg}")
    
    def complete_login(self, text, line, begidx, endidx):
        """Autocomplete cow names for login command"""
        cows = self.get_cows_list()
        if not text:
            return cows
        return [cow for cow in cows if cow.startswith(text)]
    
    def do_say(self, arg):
        """Send a message to a specific cow: say <cow> <message>"""
        if not arg:
            return
        
        response = self.send_command(f"say {arg}")
    
    def complete_say(self, text, line, begidx, endidx):
        """Autocomplete cow names for say command"""
        args = (line + '.').split()
        if len(args) == 2:
            who_list = self.get_who_list()
            if not text:
                return who_list
            return [cow for cow in who_list if cow.startswith(text)]
        return []
    
    def do_yield(self, arg):
        """Send a message to all registered cows: yield <message>"""
        if not arg:
            return
        
        response = self.send_command(f"yield {arg}")
    
    def do_who(self, arg):
        """Show registered cows"""
        response = self.send_command("who")
        if response:
            print(f"{response}")
    
    def do_cows(self, arg):
        """Show available cows"""
        response = self.send_command("cows")
        if response:
            print(f"{response}")
    
    def do_quit(self, arg):
        """Quit the chat"""
        if self.connected:
            self.send_command("quit")
        self.running = False
        if self.sock:
            self.sock.close()
        return True
    
    def do_EOF(self, arg):
        """Handle Ctrl-D"""
        return self.do_quit(arg)
    
    def default(self, line):
        """Handle unknown commands"""
        print(f"Incorrect command!")

def main():
    import sys
    
    host = "localhost" if len(sys.argv) < 2 else sys.argv[1]
    port = 1337 if len(sys.argv) < 3 else int(sys.argv[2])
    
    client = CowChatClient(host, port)
    
    if client.connect():
        # Enable tab completion
        readline.parse_and_bind("tab: complete")
        
        try:
            client.cmdloop()
        except KeyboardInterrupt:
            print("\nInterrupted")
            client.do_quit("")
    else:
        print("Failed to connect to server")

if __name__ == "__main__":
    main()
