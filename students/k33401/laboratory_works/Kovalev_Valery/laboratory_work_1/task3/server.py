import socket


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def serve_forever(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            while True:
                client, address = self.server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            self.server.close()

    def serve_client(self, client):
        html = self.handle_request()
        self.send_response(client, html)
        client.close()

    def handle_request(self):
        with open("index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, client, html):
        client.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode())


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2000, 'example.com').serve_forever()
