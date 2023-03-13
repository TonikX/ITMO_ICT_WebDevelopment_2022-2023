import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5678))
client_socket.sendall('Hello, server'.encode())
data = client_socket.recv(1024).decode()
print(data)
