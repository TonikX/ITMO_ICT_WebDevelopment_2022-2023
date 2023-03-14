import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 8888))
conn.send('Hello, server!'.encode())
data = conn.recv(1024)
print(data.decode('utf-8'))
conn.close()