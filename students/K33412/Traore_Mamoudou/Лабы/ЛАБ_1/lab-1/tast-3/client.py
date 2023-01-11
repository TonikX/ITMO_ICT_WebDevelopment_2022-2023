import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 7779))
result = conn.recv(10000)
print(result.decode())
conn.close()