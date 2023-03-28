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
                client, address = server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            server.close()

    def serve_client(self, client):
        html = self.handle_request()
        self.send_response(client, html)
        client.close()

    def handle_request(self):
        with open("task3/index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, client, html):
        client.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode("utf-8"))


if __name__ == '__main__':
    host = "localhost"
    port = 2468
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
