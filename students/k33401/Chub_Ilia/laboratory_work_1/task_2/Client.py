import Configs
import sys

sys.path.append('..')
from Base.UDPClient import *


class Client(UDPClient):
    def handle_message(self, message: str):
        self.close_socket()


if __name__ == "__main__":
    client = Client(server_socket_address=Configs.server_socket_address)
    first_side = input("The first side: ")
    second_side = input("The second side: ")
    message = f"{first_side} {second_side}"

    def failure_closure():
        print("Hehe")

    client.send_message(message=message)
    client.receive_message(failure_closure=failure_closure)
