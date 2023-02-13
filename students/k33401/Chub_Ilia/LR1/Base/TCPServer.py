from . BaseServer import *


class TCPServer(BaseServer):
    class Constants:
        default_number_to_listen = 1

    number_to_listening: int

    def __init__(
        self,
        socket_address: SocketAddress,
        buffer_size: int = BaseServer.Constants.default_buffer_size,
        number_to_listening: int = Constants.default_number_to_listen
    ):
        self.number_to_listening = number_to_listening

        super().__init__(socket_address=socket_address, buffer_size=buffer_size)

    def init_setup(self, socket_address: SocketAddress):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_STREAM)

        super().init_setup(socket_address=socket_address)

        self.socket.listen(self.number_to_listening)

    def try_listening(self):
        client_socket, client_socket_address = self.socket.accept()

        data = client_socket.recv(self.buffer_size)

        self.last_client_socket = client_socket
        self.handle_receive_message_success(data=data, client_socket_address=client_socket_address)

    def close_connection(self):
        if self.last_client_socket is not None:
            self.last_client_socket.close()
