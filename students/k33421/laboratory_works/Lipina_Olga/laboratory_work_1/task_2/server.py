import socket
from math import sqrt

def solve_eq(a: float, b: float, c: float):
    d = b**2 - 4*a*c
    return (-b-sqrt(d)) / (2*a), (-b+sqrt(d)) / (2*a)

if __name__ == "__main__":
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(('', 9090))
    sock.listen(1)
    conn, addr = sock.accept() # new socket, client address

    while True:
        data = conn.recv(1024)
        if not data:
            break
        a, b,c = map(float, data.decode().split())
        result = solve_eq(a,b,c)
        msg = f'{result[0]} {result[1]}'.encode()
        conn.send(msg)

    conn.close()

