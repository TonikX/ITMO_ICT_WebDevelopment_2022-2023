import Configs
import sys

sys.path.append('..')
from Base.BaseServer import *


class Server(BaseServer):
    def handle_message(self, message: str):
        first_side, second_size = map(int, message.split(' '))
        hypotenuse = (first_side ** 2 + second_size ** 2) ** 0.5

        print(f"THE RESULT {hypotenuse} WAS SENT TO THE CLIENT\n---\n")

        self.send_message(message=str(hypotenuse), client_socket_address=self.last_client_socket_address)


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
