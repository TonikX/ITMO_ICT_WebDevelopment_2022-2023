from Lr1.server import Server


class ThirdTaskServer(Server):
    def start(self):
        client_socket, address = self.accept_connection()

        self._get_content()
        self._send_page_to_client(client_socket)

        client_socket.close()
        self.socket.close()

    def _get_content(self):
        with open("index.html", "r") as file:
            self.content = file.read()

    def _send_page_to_client(self, client_socket):
        page_info = f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{self.content}'
        self.send_data_to_client(client_socket, page_info)

    def __init__(self, protocol_type: str):
        super().__init__(protocol_type)
        self.content = ""


if __name__ == '__main__':
    server = ThirdTaskServer("TCP")
    server.start()