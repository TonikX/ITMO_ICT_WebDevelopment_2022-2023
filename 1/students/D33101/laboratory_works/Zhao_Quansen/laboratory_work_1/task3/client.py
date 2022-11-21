from socket import *

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

socket.send('адрес страницы'.encode())
adress = socket.recv(1024)
print(adress.decode())

socket.close()