import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 9090))

msg = sock.recv(1024)
print(msg.decode("utf-8"))

sock.close()