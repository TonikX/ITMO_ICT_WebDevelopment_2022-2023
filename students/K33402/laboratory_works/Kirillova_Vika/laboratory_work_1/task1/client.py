import socket

client = socket.socket()
client.connect (("127.0.0.1", 3300))

client.send("Hello, server".encode("utf-8"))

data = client.recv(1024)
print(data.decode("utf-8"))
