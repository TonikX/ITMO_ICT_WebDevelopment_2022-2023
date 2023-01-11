import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()