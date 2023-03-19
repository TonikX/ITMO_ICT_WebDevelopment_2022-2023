import threading
import sys

sys.path.append('..')
from Base.TCPServer import *


class AsyncTCPServer(TCPServer):
    def handle_accept(self, client_socket: socket_module.socket):
        self.save_client(client_socket=client_socket)
        self.start_listen_client_thread(client_socket=client_socket)

    def start_listen_client_thread(self, client_socket: socket_module.socket):
        listen_client_thread = threading.Thread(target=self.listen_client, kwargs={"client_socket": client_socket})

        listen_client_thread.start()

    def listen_client(self, client_socket: socket_module.socket):
        while client_socket in self.get_client_sockets():
            self.get_message(client_socket=client_socket)

    def get_client_sockets(self) -> [socket_module.socket]:
        raise Exception("Method must be override in a child class")

    def save_client(self, client_socket: socket_module.socket):
        raise Exception("Method must be override in a child class")
