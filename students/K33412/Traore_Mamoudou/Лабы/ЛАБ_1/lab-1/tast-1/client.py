import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(b"Hello, server! \n")

data = sock.recv(16384)
print(data.decode("utf-8"))
sock.close()
