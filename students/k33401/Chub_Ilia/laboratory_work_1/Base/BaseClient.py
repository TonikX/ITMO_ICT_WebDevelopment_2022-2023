from . Types import *
from typing import Callable
import socket as socket_module

class BaseClient:
    class Constants:
        default_timeout = 3
        default_buffer_size = 1024

    socket: socket_module
    server_socket_address: SocketAddress
    buffer_size: int

    def __init__(
        self,
        server_socket_address: SocketAddress,
        timeout: int = Constants.default_timeout,
        buffer_size: int = Constants.default_buffer_size
    ):
        self.server_socket_address = server_socket_address
        self.buffer_size = buffer_size

        self.init_setup(timeout=timeout)

    def init_setup(self, timeout: int):
        self.socket.settimeout(timeout)

    def send_message(self, message: str):
        try:
            encoded_message = str.encode(message)

            self.try_send_message(message=encoded_message)
        except BaseException as error:
            self.handle_error(error=error)

    def receive_message(self, failure_closure: Callable):
        try:
            encoded_message = self.try_receive_message()
            decoded_message = bytes.decode(encoded_message)

            self.log_received_message(message=decoded_message)
            self.handle_message(message=decoded_message)
        except BaseException as error:
            failure_closure()
            self.handle_error(error=error)

    def log_received_message(self, message: str):
        print(f"\nANSWER FROM SERVER\nANSWER: {message}\n---\n")

    def handle_error(self, error: BaseException):
        print(f"\nERROR: {error}")
        self.close_socket()

    def close_socket(self):
        self.socket.close()
        print("SOCKET IS CLOSED")

    def try_send_message(self, message: bytes):
        raise Exception("Method must be override in a child class")

    def try_receive_message(self) -> bytes:
        raise Exception("Method must be override in a child class")

    def handle_message(self, message: str):
        raise Exception("Method must be override in a child class")
