import socket


class Client:
    def __init__(self, protocol_type: str):
        if protocol_type == "UDP":
            self.socket = self.__create_UDP_socket()
        elif protocol_type == "TCP":
            self.socket = self.__create_TCP_socket()

    def __create_TCP_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((socket.gethostname(), 1234))

        return sock

    def __create_UDP_socket(self):
        sock = socket.socket()
        sock.connect((socket.gethostname(), 1234))

        return sock

    def get_str_data(self) -> str:
        encoded_data = self.socket.recv(1024)
        data = encoded_data.decode("utf-8")

        return data
