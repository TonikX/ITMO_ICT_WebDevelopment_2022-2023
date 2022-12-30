import socket

server = socket.socket()
host = '127.0.0.1'
port = 8080
server.bind((host, port))
server.listen(3)

conn, addr = server.accept()
a_bin = conn.recv(2000)
b_bin = conn.recv(2000)
a = a_bin.decode('utf-8')
b = b_bin.decode('utf-8')
c = int(a) * int(b)
conn.send(str(c).encode())
conn.close()