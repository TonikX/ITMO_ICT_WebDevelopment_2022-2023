import socket


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(("localhost", 9092))

    s, h = input(
        "Enter the side and height of the par-gram separated by a space: "
    ).split()
    sock.sendall(str.encode("\n".join([str(s), str(h)])))

    data = sock.recv(1024)
    sock.close()

    print(data.decode())


if __name__ == "__main__":
    main()
