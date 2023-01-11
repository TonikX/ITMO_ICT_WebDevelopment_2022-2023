import socket
import sys
from threading import Thread


class ChatServer:

    def __init__(self, host: str, port: int):
        self.clients = []
        self.host = host
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _shutdown(self):
        for sock in self.clients:
            sock.close()
        self.conn.close()
        sys.exit(0)

    def _client_broadcast(self, message: bytes, sender: socket.socket) -> None:
        # Broadcast a message from a client to all the other clients
        for sock in self.clients.copy():
            if sock != sender:
                try:
                    sock.send(message)
                except OSError:
                    # Client disconnected
                    print("Someone disconnected")
                    self.clients.remove(sock)

    def _client_listen(self, sock: socket.socket) -> None:
        # Listen for messages from client
        sock.settimeout(30)
        while True:
            try:
                message = sock.recv(16384)
                print(message.decode())
                self._client_broadcast(message, sock)
            except OSError:
                sock.close()
                break

    def _main(self) -> None:
        # Run server
        self.conn.bind((self.host, self.port))
        self.conn.listen(10)
        while True:
            try:
                # Accept connection
                sock, address = self.conn.accept()
                print(f"Connection at {address}")
                # Create thread for client
                self.clients.append(sock)
                Thread(target=self._client_listen, args=(sock,)).start()
            except KeyboardInterrupt:
                self._shutdown()

    def run(self) -> None:
        # Wrapper to start thread for _main()
        Thread(target=self._main).start()


if __name__ == '__main__':
    print("Starting server...")
    server = ChatServer('127.0.0.1', 14900)
    server.run()
    print("Server started")
