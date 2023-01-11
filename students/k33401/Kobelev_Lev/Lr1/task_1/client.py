import socket


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serverAddressPort = ("localhost", 9091)

    sock.sendto(str.encode("Hello, server!"), serverAddressPort)

    data, address = sock.recvfrom(1024)
    print(data.decode())


if __name__ == "__main__":
    main()
