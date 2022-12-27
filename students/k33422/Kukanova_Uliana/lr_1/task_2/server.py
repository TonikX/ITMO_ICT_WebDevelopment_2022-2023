import socket
import math

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
server.bind((host, port))
server.listen(3)

conn, addr = server.accept()
a_bin = conn.recv(200)
b_bin = conn.recv(200)
a = a_bin.decode('utf-8')
b = b_bin.decode('utf-8')
c = math.sqrt(int(a)**2 + int(b)**2)
conn.send(str(c).encode())
conn.close()