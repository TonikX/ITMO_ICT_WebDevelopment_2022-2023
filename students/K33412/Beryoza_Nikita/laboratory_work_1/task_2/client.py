from socket import *
import sys

LOCALHOST = "127.0.0.1"
PORT = 3000

tcp_socket = socket(AF_INET, SOCK_STREAM)


def connectServer():
    tcp_socket.connect((LOCALHOST, PORT))


data = input("Введите длинны оснований трапеции и высоту трапеции в таком формате 'a b h'\n")
if not data:
    sys.exit(1)

while True:
    connectServer()
    data = str.encode(data)
    tcp_socket.send(data)
    data = tcp_socket.recv(4096)
    data = data.decode("utf-8")
    print(data)
    tcp_socket.close()
    break

