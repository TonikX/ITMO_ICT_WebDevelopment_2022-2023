from . BaseClient import *


class UDPClient(BaseClient):
    def init_setup(self, timeout: int):
        self.socket = socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)

        super().init_setup(timeout=timeout)

    def try_send_message(self, message: bytes):
        self.socket.sendto(message, self.server_socket_address)

    def try_receive_message(self) -> bytes:
        return self.socket.recvfrom(self.buffer_size)[0]
