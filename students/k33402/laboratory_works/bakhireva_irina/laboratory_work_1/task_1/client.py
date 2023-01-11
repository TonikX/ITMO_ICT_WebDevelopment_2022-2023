import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 9090))
sock.send(b"Hello, server!")

msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()