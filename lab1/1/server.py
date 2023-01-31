import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))

    print("UDP server up and listening")
    while True:
        message, addr = conn.recvfrom(SOCKET_BUFF_SIZE)

        print(f"Message from client: {message.decode('utf-8')}")
        print(f"Client address: {addr}")

        conn.sendto(b'Hello, client', addr)
        break
