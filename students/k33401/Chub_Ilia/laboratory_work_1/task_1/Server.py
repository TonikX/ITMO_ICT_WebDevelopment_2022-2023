import Configs
import sys

sys.path.append('..')
from Base.UDPServer import *


class Server(UDPServer):
    def handle_message(self, message: str, client_socket_address: SocketAddress):
        self.send_message(message=Configs.server_message, client_socket_address=self.last_client_socket_address)


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
