import socket as socket_module
from typing import Optional
from . Types import *


class BaseServer:
    class Constants:
        default_buffer_size = 1024

    socket: socket_module.socket
    socket_address: SocketAddress
    buffer_size: int

    def __init__(self, socket_address: SocketAddress, buffer_size: int = Constants.default_buffer_size):
        self.socket_address = socket_address
        self.buffer_size = buffer_size
        self.socket = self.create_socket(socket_address=socket_address)

        self.socket.bind(socket_address)

    def listen(self):
        print(f"LISTENING ON: {self.socket_address}\n")

        is_listening = True

        while is_listening:
            try:
                self.try_listening()
            except BaseException as error:
                self.handle_error(error=error)

                is_listening = False

    def handle_receive_message_success(self, data: bytes, client_socket_address: SocketAddress):
        decoded_message = bytes.decode(data)

        print(f"\n---\nNEW MESSAGE FROM CLIENT\nADDRESS: {client_socket_address}\nMESSAGE: {decoded_message}")

        self.handle_message(message=decoded_message, client_socket_address=client_socket_address)

    def encode_message(self, message: str) -> bytes:
        return str.encode(message)

    def close_socket(self):
        self.socket.close()
        print("SOCKET IS CLOSED")

    def handle_error(self, error: BaseException):
        print(f"\nERROR: {error}")
        self.close_socket()

    def create_socket(self, socket_address: SocketAddress):
        raise Exception("Method must be override in a child class")

    def try_listening(self):
        raise Exception("Method must be override in a child class")

    def handle_message(self, message: str, client_socket_address: SocketAddress):
        raise Exception("Method must be override in a child class")
