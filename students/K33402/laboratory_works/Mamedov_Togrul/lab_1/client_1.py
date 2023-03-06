import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
sock.send('Hello, server'.encode('utf-8'))

data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()