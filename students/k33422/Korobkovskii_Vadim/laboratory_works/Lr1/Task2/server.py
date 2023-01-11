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
        connection.sendto("Upper base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        a = float(data)
    while not b:
        connection.sendto("Lower base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        b = float(data)
    while not h:
        connection.sendto("The height of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        h = float(data)

    area = 0.5 * (a + b) * h
    connection.sendto(str.encode(f"The area of this trapezoid is {area}", encoding="utf-8"), address)

connection.close()