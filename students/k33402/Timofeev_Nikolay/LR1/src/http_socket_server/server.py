import socket


class HTTPServer:
    def __init__(self, host: str, port: int, name: str) -> None:
        self._host, self._port = host, port
        self._name: str = name
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def serve_forever(self) -> None:
        try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, address = self._server.accept()
                self._serve_client(client)
        except KeyboardInterrupt:
            self._server.close()

    def _serve_client(self, client) -> None:
        html = self._handle_request()
        self._send_response(client, html)

    @staticmethod
    def _handle_request(filename: str = 'index.html') -> str:
        with open(filename, "r") as file:
            body = file.read()
        return body

    @staticmethod
    def _send_response(client: socket.socket, document: str) -> None:
        client.sendall(
            f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{document}'.encode()
        )


if __name__ == '__main__':
    host = ('127.0.0.1', 2000)
    print(f'server started at http://{host[0]}:{host[1]}')
    HTTPServer(*host, 'example.com').serve_forever()
