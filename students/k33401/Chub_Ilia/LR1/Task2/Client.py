import Configs
import sys

sys.path.append('..')
from Base.BaseClient import *


class Client(BaseClient):
    def handle_message(self, message: str):
        self.close_connection()


if __name__ == "__main__":
    client = Client()
    first_side = input("The first side: ")
    second_side = input("The second side: ")
    message = f"{first_side} {second_side}"

    client.send_message(message=message, receiver_socket_address=Configs.server_socket_address)
