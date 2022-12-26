import socket

sock = socket.socket()
sock.connect(('localhost', 7777))
sock.send('Hello, server'.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))