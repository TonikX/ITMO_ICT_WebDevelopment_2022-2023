import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9090))

print(client.recv(1024).decode('utf-8'))

client.close()