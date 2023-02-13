import Configs
import sys

sys.path.append('..')
from Base.BaseClient import *


class Client(BaseClient):
    def handle_message(self, message: str):
        self.close_connection()


if __name__ == "__main__":
    client = Client()

    client.send_message(message=Configs.client_message, receiver_socket_address=Configs.server_socket_address)
