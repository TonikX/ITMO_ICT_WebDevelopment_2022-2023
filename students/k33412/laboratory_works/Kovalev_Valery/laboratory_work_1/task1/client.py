import socket


def client():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))
    sock.send(b'Hello, server!')

    data = sock.recv(1024)
    sock.close()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    client()
