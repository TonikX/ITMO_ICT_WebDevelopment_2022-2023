import socket

s = socket.socket()
s.bind(('127.0.0.1', 8888))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024)
conn.send('Hello, client!'.encode())
print(data.decode('utf-8'))
conn.close()