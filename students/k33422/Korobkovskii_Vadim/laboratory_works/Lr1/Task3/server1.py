import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.host, self.port)
        try:
            server.bind(address)
            server.listen()
            while True:
                connection, address = server.accept()
                self.serve_client(connection)
        except KeyboardInterrupt:
            server.close()

    def serve_client(self, connection):
        html = self.handle_request()
        self.send_response(connection, html)
        connection.close()

    def handle_request(self):
        with open("index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, connection, html):
        data = "HTTP/1.1 200 OK\n\nContent-Type: text/html\n\n"
        connection.sendall(f'{data}{html}'.encode("utf-8"))


if __name__ == '__main__':
    host = "localhost"
    port = 2468
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
