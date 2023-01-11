import socket
import sys
from threading import Thread


class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _send(self):
        # Threaded function for sending messages
        while True:
            try:
                msg = input()
                if msg:
                    self.conn.send(f"{self.username}: {msg}".encode())
            except (KeyboardInterrupt, EOFError):
                self.conn.close()
                sys.exit(0)

    def _recieve(self):
        # Threaded function for recieving messages
        while True:
            try:
                msg = self.conn.recv(16384).decode()
                if msg:
                    print(msg)
            except KeyboardInterrupt:
                self.conn.close()
                sys.exit(0)
            except ConnectionError:
                # Unexpected connection error
                print("Connection error")
                self.conn.close()
                sys.exit(1)

    def run(self):
        # Connect
        self.conn.connect((self.host, self.port))
        # Run threaded functions
        Thread(target=self._send).start()
        Thread(target=self._recieve).start()


if __name__ == '__main__':
    u = input("Your username: ")
    print(f"Hello {u}")
    print("Connecting to server...")
    client = ChatClient('127.0.0.1', 14900, u)
    client.run()

