import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"Received data: {self.data.decode()}")
        if self.data.decode() == "Hello, server":
            self.request.sendall(b"Hello, client")
        else:
            self.request.sendall(b"Try again")


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
