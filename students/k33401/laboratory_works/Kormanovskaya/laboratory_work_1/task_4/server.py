from typing import Dict

from config import *


class Chat:
    def __init__(self, host, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((HOST, PORT))
        self.users: Dict[socket.socket, str] = dict()

    def broadcast(self, msg: str, username: str):
        for un in self.users:
            if self.users[un] == username:
                continue
            un.send(f"{username}: {msg}".encode(FORMAT))

    def handle(self, user: socket.socket):
        while True:
            try:
                msg = user.recv(BUFFER_SIZE).decode(FORMAT)
                self.broadcast(msg, self.users[user])
            except OSError:
                user.close()
                msg = f"{self.users[user]} has left the chat :'("
                self.users.pop(user)
                self.broadcast(msg, '[sys]')
                break

    def run(self):
        self.s.listen()
        print(f"[STARTED] server is working on {HOST}:{PORT}")
        while True:
            conn, addr = self.s.accept()
            print(f"[NEW CONNECTION]: {addr[0]}:{addr[1]}")
            conn.send(ASKING.encode(FORMAT))
            username = conn.recv(1024).decode(FORMAT)
            self.users[conn] = username
            self.broadcast(f"{username} has connected to the chat", "[sys]")
            thread = Thread(target=self.handle, args=[conn])
            thread.start()


def main():
    print('Server is starting...')
    chat = Chat(HOST, PORT)
    chat.run()


if __name__ == "__main__":
    main()
