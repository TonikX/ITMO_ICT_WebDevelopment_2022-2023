import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
sock.send(b"Hello, server\n")
data = sock.recv(16384)
res = data.decode('utf-8')
print(res)
sock.close()