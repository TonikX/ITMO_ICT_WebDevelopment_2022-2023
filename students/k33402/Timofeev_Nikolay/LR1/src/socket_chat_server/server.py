import socket, threading

from loguru import logger


class ChatServer:
    def __init__(self, ip: str, host: int):
        self._sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((ip, host))
        self._sock.listen()
        self._clients: dict[socket.socket, str] = {}

    def _broadcast(self, message: str):
        for client in self._clients.keys():
            client.send(message.encode())

    def _handle_client(self, client: socket.socket):
        while True:
            try:
                message = client.recv(1024).decode()
                if message == '/quit' or not message:
                    client.close()
                else:
                    self._broadcast(f"{self._clients[client]}: {message}")
            except Exception as e:
                msg = f'{self._clients[client]} left chat'
                client.close()
                self._clients.pop(client)
                self._broadcast(msg)
                logger.info(msg)
                break

    def _receive(self):
        logger.info(f"Server working on {self._sock.getsockname()}")

        while True:
            client, address = self._sock.accept()
            logger.info(f"{str(address)} connected!")
            alias = client.recv(1024).decode()
            self._clients[client] = alias
            self._broadcast(f"{alias} connected. Send /quit to disconnect")
            thread = threading.Thread(target=self._handle_client, args=(client,))
            thread.start()

    def run(self):
        try:
            self._receive()
        except KeyboardInterrupt:
            logger.critical("Server stopped by sigterm")


if __name__ == "__main__":
    ChatServer("127.0.0.1", 9095).run()
