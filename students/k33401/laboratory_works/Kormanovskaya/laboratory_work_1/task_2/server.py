from config import *
from math import sqrt


def calculate(a: float, b: float, c: float) -> str:
    d = b * b - 4 * a * c
    if d < 0:
        return 'No real roots'
    else:
        return ', '.join(str(r) for r in {(-b - sqrt(d)) / 2 / a, (-b + sqrt(d)) / 2 / a})


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen(1)
    print(f"[STARTED] Server is listening on {HOST}")
    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE)
        print(f"[NEW REQUEST from {addr[0]}:{addr[1]}]: {data.decode(FORMAT)}")
        if not data:
            break
        try:
            values = [float(i) for i in data.decode(FORMAT).split(' ')]
            if len(values) != 3:
                raise ValueError
            conn.sendall(calculate(*values).encode(FORMAT))
        except ValueError:
            conn.sendall(MISTAKE.encode(FORMAT))
        print("the result was sent!")
        conn.close()


if __name__ == "__main__":
    main()
