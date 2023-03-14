import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4457))
sock.send('Hello, server!'.encode())

data = sock.recv(1024)
sock.close()

print (data)
