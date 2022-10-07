import socket
import typing as tp


class Server:
    def __init__(self, protocol_type: str):
        if protocol_type == "UDP":
            self.socket = self.__create_UDP_socket()
        elif protocol_type == "TCP":
            self.socket = self.__create_TCP_socket()

    def __create_TCP_socket(self) -> socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def __create_UDP_socket(self):
        sock = socket.socket()
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def get_data(self, client_socket: socket) -> tp.List[str]:
        data = []
        while True:
            encoded_data = client_socket.recv(1024)
            if len(encoded_data) <= 0:
                break
            data.append(encoded_data.decode("utf-8"))

        return data

    def accept_connection(self) -> (socket, tp.Any):
        return self.socket.accept()
