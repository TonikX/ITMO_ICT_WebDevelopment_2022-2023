import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5002))

data = sock.recv(4096)
print(data.decode('utf-8'))
sock.close()