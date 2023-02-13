import socket as socket_module
from . Types import *


class BaseClient:
    class Constants:
        default_timeout = 3
        default_buffer_size = 1024

    socket: socket_module
    buffer_size: int

    def __init__(self, timeout: int = Constants.default_timeout, buffer_size: int = Constants.default_buffer_size):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)
        self.socket.settimeout(timeout)
        self.buffer_size = buffer_size

    def send_message(self, message: str, receiver_socket_address: SocketAddress):
        try:
            encoded_message = str.encode(message)

            self.socket.sendto(encoded_message, receiver_socket_address)
            self.receive_message()
        except KeyboardInterrupt:
            print("\nKEYBOARD INTERRUPT")
            self.close_connection()
        except Exception as error:
            print(f"ERROR: {error}")
            self.close_connection()

    def receive_message(self):
        server_data, server_address = self.socket.recvfrom(self.buffer_size)
        decoded_message = bytes.decode(server_data)

        print(f"ANSWER FROM SERVER\nADDRESS: {server_address}\nANSWER: {decoded_message}\n---\n")

        self.handle_message(message=decoded_message)

    def handle_message(self, message: str):
        raise Exception("Method must be override in a child class")

    def close_connection(self):
        self.socket.close()
        print("CONNECTION CLOSED")
