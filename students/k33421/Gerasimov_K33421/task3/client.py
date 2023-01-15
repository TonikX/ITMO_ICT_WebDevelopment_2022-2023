import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 9090))
data = s.recv(9111989)
print(data.decode('utf-8'))
s.close()