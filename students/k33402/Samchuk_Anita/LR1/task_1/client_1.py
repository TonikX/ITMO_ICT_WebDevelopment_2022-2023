import socket

sock = socket.socket()
sock.connect( ('', 9090) )
sock.send(b'Hello, server')

data = sock.recv(1024)
sock.close

print(data.decode('utf-8'))
