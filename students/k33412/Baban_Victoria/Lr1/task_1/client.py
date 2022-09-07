import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send(b'Hello, server.\n')

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()

