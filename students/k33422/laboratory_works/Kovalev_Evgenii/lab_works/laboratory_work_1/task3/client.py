import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2468))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()