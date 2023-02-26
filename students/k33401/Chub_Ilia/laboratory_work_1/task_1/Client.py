import Configs
import sys

sys.path.append('..')
from Base.UDPClient import *


class Client(UDPClient):
    def handle_message(self, message: str):
        self.close_socket()


if __name__ == "__main__":
    client = Client(server_socket_address=Configs.server_socket_address)

    client.send_message(message=Configs.client_message)
    client.receive_message()
