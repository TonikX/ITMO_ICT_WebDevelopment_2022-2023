from config import *

CONNECT_MSG = "Hello, client!"


def main():
    UDPServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPServer.bind(ADDR)
    print(f"[STARTED] server is working on {HOST}:{PORT}")
    while True:
        msg, addr = UDPServer.recvfrom(BUFFER_SIZE)
        print(f"[{addr[0]}:{addr[1]}]: {msg.decode(FORMAT)}")
        UDPServer.sendto(CONNECT_MSG.encode(FORMAT), addr)


if __name__ == "__main__":
    main()
