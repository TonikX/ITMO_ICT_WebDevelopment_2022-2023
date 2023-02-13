import Configs
import sys

sys.path.append('..')
from Base.UDPServer import UDPServer


class Server(UDPServer):
    def handle_message(self, message: str):
        first_side, second_size = map(int, message.split(' '))
        hypotenuse = (first_side ** 2 + second_size ** 2) ** 0.5
        answer = str(hypotenuse)

        self.send_message_by_client_socket_address(
            message=answer,
            client_socket_address=self.last_client_socket_address
        )
        print(f"THE RESULT {hypotenuse} WAS SENT TO THE CLIENT\n---\n")


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
