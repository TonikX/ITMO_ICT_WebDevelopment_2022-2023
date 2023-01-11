import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(5)

while True:
    try:
        conn, addr = sock.accept()
        a, b = [int(i) for i in conn.recv(1024).decode('utf-8').split('\n')]
        c = math.sqrt(a*a+b*b)
        conn.send(str.encode(str(c)))
    finally:
        sock.close()
        break
