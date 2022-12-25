import socket

from _config import *

if __name__ == '__main__':
    print('Solving Pythagorean theorem')
    params = input('Enter a, b [space-separated]: ')
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((SOCKET_ADDR, SOCKET_PORT))

    conn.send(params.encode('utf-8'))

    message, server = conn.recvfrom(SOCKET_BUFF_SIZE)
    print(f"Message from server: {message.decode('utf-8')}")

    conn.close()
