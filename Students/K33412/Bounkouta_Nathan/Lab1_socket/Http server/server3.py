import socket

conn = socket.socket()

conn.connect(("192.168.1.5", 8000))
result = conn.recv(10000)
print(result.decode())
conn.close()