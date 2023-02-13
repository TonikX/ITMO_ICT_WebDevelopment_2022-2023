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

    def __init__(self, socket_address: SocketAddress, buffer_size: int = Constants.default_buffer_size):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)
        self.socket_address = socket_address
        self.buffer_size = buffer_size
        self.last_client_socket_address = None

        self.socket.bind(socket_address)

    def listen(self):
        print(f"LISTENING ON: {self.socket_address}\n")

        is_listening = True

        while is_listening:
            try:
                data, client_socket_address = self.socket.recvfrom(self.buffer_size)

                self.handle_listening_success(data=data, client_socket_address=client_socket_address)
            except BaseException as error:
                self.handle_listening_error(error=error)

                is_listening = False

    def handle_listening_success(self, data: bytes, client_socket_address: SocketAddress):
        decoded_message = bytes.decode(data)
        self.last_client_socket_address = client_socket_address

        print(f"NEW MESSAGE FROM CLIENT\nADDRESS: {client_socket_address}\nMESSAGE: {decoded_message}\n---\n")

        self.handle_message(message=decoded_message)

    def handle_message(self, message: str):
        raise Exception("Method must be override in a child class")

    def handle_listening_error(self, error: BaseException):
        print(f"\nERROR: {error}")
        self.close_connection()

    def send_message(self, message: str, client_socket_address: SocketAddress):
        encoded_message = str.encode(message)

        self.socket.sendto(encoded_message, client_socket_address)

    def close_connection(self):
        self.socket.close()
        print("STOP LISTENING")
