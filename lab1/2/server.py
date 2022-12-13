import socket

from _config import *


def parse_params(params):
    return list(map(int, params.split(' ')))


def solve_pythagorean(a, b):
    return (a ** 2 + b ** 2) ** 0.5


if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))
    conn.listen(10)

    print("TCP server up and listening")
    while True:
        try:
            client_socket, addr = conn.accept()
            message = client_socket.recv(SOCKET_BUFF_SIZE)

            params = message.decode('utf-8')
            print(f"Message from client: {params}")
            print(f"Client address: {addr}")

            a, b = parse_params(params)
            result = str(solve_pythagorean(a, b))

            client_socket.send(result.encode('utf-8'))
        except:
            break
    conn.close()
