import socket


class Client:
    def __init__(self):
        self.socket = self.create_socket()

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((socket.gethostname(), 1234))

        return sock

    def get_data(self) -> str:
        encoded_data = self.socket.recv(1024)
        data = encoded_data.decode("utf-8")

        return data

    def start(self):
        self.socket.send(b"Hello, server")

        server_data = self.get_data()
        print(server_data)

        self.socket.close()


client = Client()
client.start()
