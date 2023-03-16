import socket

conn = socket.socket()

conn.connect(("localhost", 62102))
result = conn.recv(10000)
print(result.decode())
conn.close()
