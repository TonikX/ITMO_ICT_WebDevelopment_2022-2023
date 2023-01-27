import socket

conn = socket.socket()
conn.connect(('localhost', 9999))

conn.send(b'Hello server! \n')

data = conn.recv(1024)
print(data.decode("utf-8"))

conn.close()
