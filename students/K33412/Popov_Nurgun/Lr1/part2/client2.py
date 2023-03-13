import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5678))
msg = client_socket.recv(1024).decode()
print(msg)
parameters_str = input()
client_socket.sendall(parameters_str.encode())
data = client_socket.recv(1024).decode()
print(data)
