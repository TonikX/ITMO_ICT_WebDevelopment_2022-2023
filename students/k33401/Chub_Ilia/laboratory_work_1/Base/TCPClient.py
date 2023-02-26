from . BaseClient import *


class TCPClient(BaseClient):
    def init_setup(self, timeout: int):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_STREAM)

        super().init_setup(timeout=timeout)

    def try_send_message(self, message: bytes):
        self.socket.send(message)

    def try_receive_message(self) -> bytes:
        return self.socket.recv(self.buffer_size)

    def log_received_message(self, message: str):
        pass

    def connect(self):
        try:
            self.socket.connect(self.server_socket_address)
        except BaseException as error:
            self.handle_error(error=error)
