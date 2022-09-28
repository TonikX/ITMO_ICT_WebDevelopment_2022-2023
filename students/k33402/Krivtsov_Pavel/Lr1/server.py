import socket
import typing as tp


class Server:
    def __init__(self):
        self.socket = self.create_socket()

    def create_socket(self) -> socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def get_str_data(self, client_socket: socket) -> str:
        data = ""
        while True:
            encoded_data = client_socket.recv(1024)
            if len(encoded_data) <= 0:
                break
            data += encoded_data.decode("utf-8")

        return data

    def get_client_info(self) -> (socket, tp.Any):
        return self.socket.accept()
