from . BaseServer import *


class UDPServer(BaseServer):
    def init_setup(self, socket_address: SocketAddress):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)

        super().init_setup(socket_address=socket_address)

    def try_listening(self):
        data, client_socket_address = self.socket.recvfrom(self.buffer_size)
        self.last_client_socket_address = client_socket_address

        self.handle_receive_message_success(data=data, client_socket_address=client_socket_address)
