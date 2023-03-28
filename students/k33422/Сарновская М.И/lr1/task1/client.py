import socket


conn = socket.socket()
conn.connect(('127.0.0.1', 1024))
conn.send(b"Hello, server \n")
data = conn.recv(1024)
udata = data.decode('utf-8')
print(udata)
conn.close()