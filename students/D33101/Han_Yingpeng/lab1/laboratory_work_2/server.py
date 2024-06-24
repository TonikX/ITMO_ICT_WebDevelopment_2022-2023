import socket
import math

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp.bind(('127.0.0.1', 4800))
tcp.listen()

while True:
    client_connection, client_address = tcp.accept()
    data = client_connection.recv(1024).decode()
    data = [float(i) for i in data.split(',')]
    client_connection.send(str(math.sqrt(data[0] ** 2 + data[1] ** 2)).encode())