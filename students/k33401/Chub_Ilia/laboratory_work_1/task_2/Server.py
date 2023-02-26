import Configs
import sys

sys.path.append('..')
from Base.UDPServer import *


class Server(UDPServer):
    def handle_message(self, message: str, client_socket_address: SocketAddress):
        first_side, second_size = map(int, message.split(' '))
        hypotenuse = (first_side ** 2 + second_size ** 2) ** 0.5
        answer = str(hypotenuse)

        self.send_message(message=answer, client_socket_address=self.last_client_socket_address)


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
