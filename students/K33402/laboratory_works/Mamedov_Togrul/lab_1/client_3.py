import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2468))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()