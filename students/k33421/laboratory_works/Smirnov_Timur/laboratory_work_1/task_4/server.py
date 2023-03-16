import socket
import sys
from threading import Thread


class ChatServer:

    def __init__(self, host, port):
        self.clients = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __shutdown(self):
        for conn in self.clients:
            conn.close()
        self.sock.close()
        sys.exit(0)

    def __client_broadcast(self, message, sender):
        for conn in self.clients.copy():
            if conn != sender:
                try:
                    conn.send(message)
                except OSError:
                    print("Someone disconnected")
                    self.clients.remove(conn)

    def __client_listen(self, conn):
        conn.settimeout(30)
        while True:
            try:
                message = conn.recv(1024)
                print(message.decode())
                self.__client_broadcast(message, conn)
            except OSError:
                conn.close()
                break

    def __main(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)
        while True:
            try:
                conn, address = self.sock.accept()
                print(f"Connection at {address}")
                self.clients.append(conn)
                Thread(target=self.__client_listen, args=(conn,)).start()
            except KeyboardInterrupt:
                self.__shutdown()

    def run(self):
        Thread(target=self.__main).start()


if __name__ == '__main__':
    print("Starting server...")
    server = ChatServer('127.0.0.1', 14900)
    server.run()
    print("Server started")
