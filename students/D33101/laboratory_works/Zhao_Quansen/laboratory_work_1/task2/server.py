import socket
import math

tcp_socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_socket_host.bind(('127.0.0.1', 4245))
tcp_socket_host.listen()

while True:
    client, addr = tcp_socket_host.accept()
    data = [float(i) for i in client.recv(1024).decode().split(',')]
    a = data[0]
    b = data[1]
    c = data[2]
    dis = b ** 2 - 4 * a * c
    
    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        client.send(f'x1 = {x1}\nx2 = {x2}'.encode())
    elif dis == 0:
        x = -b / (2 * a)
        client.send(f"x = {x}".encode())
    else:
        client.send("Корней нет".encode())