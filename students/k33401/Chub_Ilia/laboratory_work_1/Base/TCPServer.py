from . BaseServer import *


class TCPServer(BaseServer):
    class Constants:
        number_to_listening = 5

    last_client_socket: Optional[socket_module.socket] = None

    def __init__(
        self,
        socket_address: SocketAddress,
        buffer_size: int = BaseServer.Constants.default_buffer_size,
        number_to_listening: int = Constants.number_to_listening
    ):
        super().__init__(socket_address=socket_address, buffer_size=buffer_size)

        self.socket.listen(number_to_listening)

    def create_socket(self, socket_address: SocketAddress) -> socket_module.socket:
        return socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_STREAM)

    def try_listening(self):
        client_socket, _ = self.socket.accept()
        self.last_client_socket = client_socket

        self.handle_accept(client_socket=client_socket)

    def get_message(self, client_socket: socket_module.socket):
        try:
            encoded_message = client_socket.recv(self.buffer_size)

            self.handle_receive_message_success(data=encoded_message, client_socket_address=client_socket.getpeername())
        except BaseException as error:
            self.handle_client_error(error=error)

    def send_message(self, message: str, client_socket: socket_module.socket):
        try:
            encoded_message = self.encode_message(message=message)

            client_socket.send(encoded_message)

            print(f"\n---\nTHE MESSAGE ({message}) HAS BEEN SENT TO {client_socket.getpeername()}")
        except BaseException as error:
            self.handle_client_error(error=error)

    def handle_client_error(self, error: BaseException):
        print(f"ERROR: {error}")
        self.remove_client()

    def remove_client(self):
        raise Exception("Method must be override in a child class")

    def handle_accept(self, client_socket: socket_module.socket):
        raise Exception("Method must be override in a child class")
