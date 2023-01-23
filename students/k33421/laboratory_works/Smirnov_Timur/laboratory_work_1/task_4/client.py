import socket
import sys
from threading import Thread


class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __send(self):
        while True:
            try:
                msg = input('>>')
                if msg:
                    self.sock.send(f"{self.username}: {msg}".encode())
            except (KeyboardInterrupt, EOFError):
                self.conn.close()
                sys.exit(0)

    def __recieve(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode()
                if msg:
                    print(msg)
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit(0)
            except ConnectionError:
                # Unexpected connection error
                print("Connection error")
                self.sock.close()
                sys.exit(1)

    def run(self):
        # Connect
        self.sock.connect((self.host, self.port))
        # Run threaded functions
        Thread(target=self.__send).start()
        Thread(target=self.__recieve).start()


if __name__ == '__main__':
    name = input("Your username: ")
    print("Connecting to server...")
    client = ChatClient('127.0.0.1', 14900, name)
    client.run()
