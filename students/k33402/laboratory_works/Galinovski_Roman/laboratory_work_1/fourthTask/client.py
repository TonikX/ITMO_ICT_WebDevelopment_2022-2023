import socket
import threading


class Client:
    def __init__(self, ip, port):
        self.nickname = ""
        self.socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketVar.connect((ip, port))

    def receive(self):
        while True:
            try:
                message = self.socketVar.recv(1024).decode()
                if message == "What's your nickname?":
                    self.socketVar.send(self.nickname.encode())
                else:
                    print(message)
            except:
                print("Error...")
                self.socketVar.close()
                break

    def send(self):
        while True:
            try:
                message = input()
                self.socketVar.send(message.encode())
            except:
                print("Error...")
                self.socketVar.close()
                break               

    def start(self):
        self.nickname = input("Enter your nickname: ")
        receiveThread = threading.Thread(target=self.receive)
        receiveThread.start()

        sendThread = threading.Thread(target=self.send)
        sendThread.start()


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9880
    Client(host, port).start()