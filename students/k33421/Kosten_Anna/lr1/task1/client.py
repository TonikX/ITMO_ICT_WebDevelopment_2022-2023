import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8080))
s.sendall('Hello, server.'.encode('utf-8'))
data = s.recv(1024)
print(data.decode('utf-8'))
s.close()