from . BaseServer import *


class UDPServer(BaseServer):
    last_client_socket_address: Optional[SocketAddress] = None

    def create_socket(self, socket_address: SocketAddress) -> socket_module.socket:
        return socket_module.socket(family=socket_module.AF_INET, type=socket_module.SOCK_DGRAM)

    def try_listening(self):
        data, client_socket_address = self.socket.recvfrom(self.buffer_size)
        self.last_client_socket_address = client_socket_address

        self.handle_receive_message_success(data=data, client_socket_address=client_socket_address)

    def send_message(self, message: str, client_socket_address: SocketAddress):
        try:
            encoded_message = self.encode_message(message=message)

            print(f"\n---\nTHE MESSAGE ({message}) HAS BEEN SENT TO {client_socket_address}")

            self.socket.sendto(encoded_message, client_socket_address)
        except BaseException as error:
            self.handle_error(error=error)
