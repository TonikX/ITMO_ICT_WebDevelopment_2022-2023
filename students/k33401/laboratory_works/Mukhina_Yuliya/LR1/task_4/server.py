import socket, threading


class MyChat:
    def __init__(self, ip, host):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, host))
        self.sock.listen()
        self.clients = {}  # {client:alias}

    def broadcast(self, message, alias):
        for client in self.clients.keys():
            client.send(f"{alias}: {message}".encode())

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
        print("Server has started")
        while True:
            client, address = self.sock.accept()
            print(f"{str(address)} connected!")
            client.send(b"What is your alias?")
            alias = client.recv(1024).decode()
            self.clients[client] = alias
            self.broadcast(f"{alias} has connected to the chat", "Server")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    MyChat("127.0.0.1", 9091).run()
