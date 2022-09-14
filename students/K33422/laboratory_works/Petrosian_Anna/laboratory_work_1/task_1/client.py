import socket

port = 14900
host = "127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((host, port))
sock.send('Hello, server')

data = sock.recv(1024)
print (data)
sock.close()