import socket as socket_module
from typing import Optional
from . Types import *


class BaseServer:
    class Constants:
        default_buffer_size = 1024

    socket: socket_module.socket
    socket_address: SocketAddress
    buffer_size: int

    last_client_socket_address: Optional[SocketAddress]
    last_client_socket: Optional[socket_module.socket]

    def __init__(self, socket_address: SocketAddress, buffer_size: int = Constants.default_buffer_size):
        self.socket_address = socket_address
        self.buffer_size = buffer_size
        self.last_client_socket_address = None
        self.last_client_socket = None

        self.init_setup(socket_address=socket_address)

    def init_setup(self, socket_address: SocketAddress):
        self.socket.bind(socket_address)

    def listen(self):
        print(f"LISTENING ON: {self.socket_address}\n")

        is_listening = True

        while is_listening:
            try:
                self.try_listening()
            except BaseException as error:
                self.handle_listening_error(error=error)

                is_listening = False

    def try_listening(self):
        raise Exception("Method must be override in a child class")

    def handle_receive_message_success(self, data: bytes, client_socket_address: SocketAddress):
        decoded_message = bytes.decode(data)

        print(f"NEW MESSAGE FROM CLIENT\nADDRESS: {client_socket_address}\nMESSAGE: {decoded_message}\n---\n")

        self.handle_message(message=decoded_message)

    def handle_message(self, message: str):
        raise Exception("Method must be override in a child class")

    def handle_listening_error(self, error: BaseException):
        print(f"\nERROR: {error}")
        self.close_connection()

    def send_message_by_client_socket_address(self, message: str, client_socket_address: SocketAddress):
        encoded_message = self.encode_message(message=message)

        self.socket.sendto(encoded_message, client_socket_address)

    def send_message_by_client_socket(self, message: str, client_socket: socket_module.socket):
        encoded_message = self.encode_message(message=message)

        client_socket.sendall(encoded_message)

    def encode_message(self, message: str) -> bytes:
        return str.encode(message)

    def close_connection(self):
        self.socket.close()
        print("SOCKET IS CLOSED")
