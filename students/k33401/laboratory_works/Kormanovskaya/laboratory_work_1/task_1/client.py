from config import *

CONNECT_MSG = "Hello, server!"


def main():
    UDPClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPClient.sendto(CONNECT_MSG.encode(FORMAT), ADDR)
    msg, addr = UDPClient.recvfrom(BUFFER_SIZE)
    print(f"[{addr[0]}:{addr[1]}]: {msg.decode(FORMAT)}")


if __name__ == "__main__":
    main()
