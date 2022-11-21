import socket


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 1234))
    sock.listen(10)

    while True:
        clientsocket, address = sock.accept()
        print(f"Connected: {address} has been established")
        clientsocket.send(str.encode(f"Hello, client!", "utf-8"))
        clientsocket.close()


if __name__ == "__main__":
    server()