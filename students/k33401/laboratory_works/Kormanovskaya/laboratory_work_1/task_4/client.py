from config import *


class User:
    def __init__(self, address):
        self.username = ""
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(address)

    def receive(self):
        while True:
            try:
                msg = self.s.recv(BUFFER_SIZE).decode(FORMAT)
                if msg == ASKING:
                    self.s.send(self.username.encode(FORMAT))
                else:
                    print(msg)
            except:
                print('Something went wrong. Disconnecting!')
                self.s.close()
                break

    def send(self):
        while True:
            msg = input()
            self.s.send(msg.encode(FORMAT))

    def start(self):
        self.username = input(ASKING)
        recv_thread = Thread(target=self.receive)
        recv_thread.start()

        send_thread = Thread(target=self.send)
        send_thread.start()


def main():
    user = User(ADDR)
    user.start()


if __name__ == "__main__":
    main()
