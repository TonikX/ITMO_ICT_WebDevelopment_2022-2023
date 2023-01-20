import socket
import threading

class Server:
    def __init__(self, ip, host):
        self.socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketVar.bind((ip, host))
        self.socketVar.listen()
        self.clients = {}

    def broadcast(self, message, nickname):
        try:
            for client in self.clients.keys():
                client.send(f"{nickname}: {message}".encode("utf-8"))
        except:
            print('Broadcast error!')


    def handleClient(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message, self.clients[client])
            except:
                client.close()
                leftClient = self.clients.pop(client)
                self.broadcast('Left the chat ', leftClient)
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
            thread = threading.Thread(target=self.handleClient, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 9880
    Server(host, port).run()