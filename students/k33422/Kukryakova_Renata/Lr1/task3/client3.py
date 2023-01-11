import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 8888))
sock.send('Hello, server'.encode("utf-8"))
s = sock.recv(1024)
print(s.decode("utf-8"))
sock.close()