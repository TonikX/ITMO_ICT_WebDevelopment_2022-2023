import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8071))
sock.listen(5)
client_socket, addr = sock.accept()
print(client_socket.recv(1024).decode("utf-8"))
client_socket.send(b"Hello, client")
sock.close()
