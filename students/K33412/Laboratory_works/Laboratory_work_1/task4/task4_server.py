import socketserver


class ThreadedTCPServer(socketserver.ThreadingTCPServer):

    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        print("Server started")
        self.receivers = set()

    def add_receiver(self, receiver):
        print("Client connected")
        self.receivers.add(receiver)

    def send_message(self, source, data):
        for receiver in self.receivers:
            if receiver.token != source.token:
                receiver.request.sendall(data)

    def remove_receiver(self, receiver):
        self.receivers.remove(receiver)


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    RECEIVER = 0
    SENDER = 1
    kind = None
    token: str = ""

    def handle(self):
        while True:
            self.data = self.request.recv(1024).strip()
            if self.data:
                print(f"Received data: {self.data.decode()}")

                if b"Kind" in self.data:

                    if b"Kind: receiver" in self.data:
                        self.server.add_receiver(self)
                        self.kind = self.RECEIVER
                    elif b"Kind: sender" in self.data:
                        self.kind = self.SENDER

                    token = self.data.decode(
                    )[self.data.decode().find("Token")+6:]
                    self.token = token

                else:
                    self.server.send_message(self, self.data)

    def finish(self):
        if self.kind == self.RECEIVER:
            self.server.remove_receiver(self)
        super().finish()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    server.serve_forever()
