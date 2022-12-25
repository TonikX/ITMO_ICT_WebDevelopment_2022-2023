import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.connect((SOCKET_ADDR, SOCKET_PORT))

    conn.send(b'Hello, server!')

    message = conn.recv(SOCKET_BUFF_SIZE)
    print(f"Message from server: {message.decode('utf-8')}")
