import socket
from math import sqrt


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return f"{(-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a}", f"{(-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a}"
    else:
        return "No real roots"


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7778))
    sock.listen()
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    a = ""
    b = ""
    c = ""
    result = ""

    while not result:
        while not a:
            conn.send('a'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                a = float(data)

        while not b:
            conn.send('b'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                b = float(data)

        while not c:
            conn.send('c'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                c = float(data)

        result = quadratic_equation(a, b, c)
        conn.send(str.encode(f"Result is {result}"))

    conn.close()


if __name__ == "__main__":
    server()
