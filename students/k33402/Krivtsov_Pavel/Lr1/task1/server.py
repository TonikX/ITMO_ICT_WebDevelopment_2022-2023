import socket


class Server:
    def __init__(self):
        self.socket = self.create_socket()

    def create_socket(self) -> socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def get_data(self, client_socket: socket) -> str:
        data = ""
        while True:
            encoded_data = client_socket.recv(1024)
            if len(encoded_data) <= 0:
                break
            data += encoded_data.decode("utf-8")

        return data

    def start(self):
        # create connection
        client_socket, address = self.socket.accept()
        client_socket.send(bytes("Hello, client", "utf-8"))

        client_data = self.get_data(client_socket)
        print(client_data)

        client_socket.close()
        self.socket.close()


server = Server()
server.start()
