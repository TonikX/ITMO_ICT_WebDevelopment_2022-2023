import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8071))
sock.send(b"Hello, server")
print(sock.recv(1024).decode("utf-8"))
sock.close()
