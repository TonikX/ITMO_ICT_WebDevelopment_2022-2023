import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6666))

sock.send(bytes("Hello, server!!!", "utf-8"))
msg = sock.recv(1024)
print(msg.decode("utf-8"))