import socket, threading

from loguru import logger


class ChatServer:
    def __init__(self, ip: str, host: int):
        self.sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, host))
        self.sock.listen()
        self.clients: dict[socket.socket, str] = {}

    def broadcast(self, message: str):
        for client in self.clients.keys():
            client.send(message.encode())

    def handle_client(self, client: socket.socket):
        while True:
            try:
                message = client.recv(1024).decode()
                if message == '/quit' or not message:
                    client.close()
                else:
                    self.broadcast(f"{self.clients[client]}: {message}")
            except Exception as e:
                msg = f'{self.clients[client]} left chat'
                client.close()
                self.clients.pop(client)
                self.broadcast(msg)
                logger.info(msg)
                break

    def receive(self):
        logger.info(f"Server working on {self.sock.getsockname()}")

        while True:
            client, address = self.sock.accept()
            logger.info(f"{str(address)} connected!")
            alias = client.recv(1024).decode()
            self.clients[client] = alias
            self.broadcast(f"{alias} connected. Send /quit to disconnect")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        try:
            self.receive()
        except KeyboardInterrupt:
            logger.critical("Server stopped by sigterm")


if __name__ == "__main__":
    ChatServer("127.0.0.1", 9095).run()
