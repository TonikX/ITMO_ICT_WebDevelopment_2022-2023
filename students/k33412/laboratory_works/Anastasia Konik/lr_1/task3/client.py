import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 8080))
client_sock.sendall('Hi!'.encode("utf-8"))

data = client_sock.recv(1024)
print(data.decode("utf-8"))

client_sock.close()