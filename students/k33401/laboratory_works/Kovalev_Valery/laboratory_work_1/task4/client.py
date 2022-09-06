import socket
import threading


class MyClient:
    def __init__(self, ip, port):
        self.alias = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()
                if message == "What is your alias?":
                    self.sock.send(self.alias.encode())
                else:
                    print(message)
            except:
                print("Error!")
                self.sock.close()
                break

    def send(self):
        while True:
            message = input()
            self.sock.send(message.encode())

    def start(self):
        self.alias = input("Enter your alias: ")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()


if __name__ == "__main__":
    MyClient("127.0.0.1", 9091).start()
