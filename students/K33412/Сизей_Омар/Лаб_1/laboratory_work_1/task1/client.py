import socket


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 1234))
    sock.send(b'Hello, server! \n')

    data = sock.recv(1234)
    sock.close()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    client()