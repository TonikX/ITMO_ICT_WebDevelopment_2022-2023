import socket
from math import sqrt

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8000))
conn.listen(10)
while True:
    try:
        clientsocket, address = conn.accept()
        data = clientsocket.recv(16384).decode("utf-8")
        a, b = map(lambda x: int(x), data.split())
        print("a = ", a, ", b = ", b)
        c = sqrt(a ** 2 + b ** 2)
        c = str(c).encode()
        clientsocket.send(c)
    except KeyboardInterrupt:
        conn.close()
        break
