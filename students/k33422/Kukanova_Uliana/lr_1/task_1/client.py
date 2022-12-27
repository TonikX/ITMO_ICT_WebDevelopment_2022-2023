import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

conn.connect(("127.0.0.1", 8080))
conn.send(b"Hello, server! \n")
data = conn.recv(2000)
udata = data.decode('utf-8')
print(udata)
conn.close()