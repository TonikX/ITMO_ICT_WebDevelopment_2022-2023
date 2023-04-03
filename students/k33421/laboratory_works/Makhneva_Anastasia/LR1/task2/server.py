import socket

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
connection, address = server.accept()

a = str()
b = str()
h = str()
area = str()

while not area:
    while not a:
        connection.sendto("upper base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        a = float(data)
    while not b:
        connection.sendto("lower base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        b = float(data)
    while not h:
        connection.sendto("height of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        h = float(data)

    area = 0.5 * (a + b) * h
    connection.sendto(str.encode(f"the area of this trapezoid is {area}", encoding="utf-8"), address)

connection.close()
