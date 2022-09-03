import socket

LOCALHOST = "127.0.0.1"
PORT = 3000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LOCALHOST, PORT))
client.send(b"Hello, world!")
client.close()

