import socket, sys


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind(("localhost", 9091))

    while True:
        data, address = sock.recvfrom(1024)
        print(data.decode())
        sock.sendto(str.encode("Hello, client!"), address)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
