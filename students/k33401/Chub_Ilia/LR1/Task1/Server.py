import Configs
import sys

sys.path.append('..')
from Base.UDPServer import UDPServer


class Server(UDPServer):
    def handle_message(self, message: str):
        self.send_message_by_client_socket_address(
            message=Configs.server_message,
            client_socket_address=self.last_client_socket_address
        )


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
