from socket import *
import sys

LOCALHOST = "127.0.0.1"
PORT = 3000

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((LOCALHOST, PORT))
tcp_socket.send("989796".encode())
res = tcp_socket.recv(4096)
res = res.decode('utf-8')


data = input(res)
if not data:
    tcp_socket.close()
    sys.exit(1)

while True:
    data = str.encode(data)
    tcp_socket.send(data)
    data = tcp_socket.recv(4096)
    data = data.decode("utf-8")
    print(data)
    tcp_socket.close()
    break

