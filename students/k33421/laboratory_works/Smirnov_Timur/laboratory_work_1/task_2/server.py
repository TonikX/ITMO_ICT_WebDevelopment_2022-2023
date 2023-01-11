import socket

# d - площадь параллелограмма


class Server:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def parallelogram_square(self, base, height):
        return int(base) * int(height)

    def send(self, msg):
        self.conn.send(msg.encode('utf-8'))

    def receive(self):
        data = self.conn.recv(1024)
        return data.decode('utf-8')

    def start(self):
        self.sock.bind(('', 9090))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def close(self):
        self.sock.close()


def main():
    srv = Server()
    srv.start()

    srv.send("Input base lenght of the parallelogram: ")
    base = srv.receive()

    srv.send("Input height of the parallelogram: ")
    height = srv.receive()

    square = srv.parallelogram_square(base, height)
    srv.send(f"Square of the parallelogram is {square}")

    srv.close()


if __name__ == '__main__':
    main()
