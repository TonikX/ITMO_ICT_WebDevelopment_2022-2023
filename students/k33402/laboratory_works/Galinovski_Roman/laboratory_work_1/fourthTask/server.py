import socket
import threading

class Chat:
    def __init__(self, ip, host):
        self.socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketVar.bind((ip, host))
        self.socketVar.listen()
        self.clients = {}  # {client:nickname}

    def broadcast(self, message, nickname):
        for client in self.clients.keys():
            client.send(f"{nickname}: {message}".encode())

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message, self.clients[client])
            except:
                client.close()
                self.broadcast(f'{self.clients[client]} has left the chat...'.encode('utf-8'))
                self.clients.pop(client)
                break

    def receive(self):
        print("Server is running")
        while True:
            client, address = self.socketVar.accept()
            print(f"{str(address)} connected!")
            client.send(b"What is your nickname?")
            nickname = client.recv(1024).decode()
            self.clients[client] = nickname
            self.broadcast(f"{nickname} has connected to the chat", "Server")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    Chat("127.0.0.1", 9980).run()