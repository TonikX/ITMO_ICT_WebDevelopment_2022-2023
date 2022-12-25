import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9523))
sock.send(b'Hello, server.\n')

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()

