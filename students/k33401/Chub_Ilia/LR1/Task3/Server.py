import Configs
import sys

sys.path.append('..')
from Base.TCPServer import *


class Server(TCPServer):
    def handle_accept(self, client_socket: socket_module.socket):
        answer = self.get_html_response()

        self.send_message(message=answer, client_socket=self.last_client_socket)
        self.last_client_socket.close()

        self.last_client_socket = None

    def get_html_response(self) -> str:
        type = "HTTP/1.1 200 OK\n"
        header = "Content-Type: text/html\n\n"

        index_html = open(Configs.html_page_file_name, 'r')
        body = index_html.read()
        index_html.close()

        return type + header + body


if __name__ == "__main__":
    server = Server(socket_address=Configs.server_socket_address)

    server.listen()
