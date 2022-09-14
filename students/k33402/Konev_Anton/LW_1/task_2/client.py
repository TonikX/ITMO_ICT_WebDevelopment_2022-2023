import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8091))
print(sock.recv(1024).decode("utf-8"))
coefs = input("Enter a, b, c divided by space: ").encode("utf-8")
sock.send(coefs)
print(sock.recv(1024).decode("utf-8"))
sock.close()
