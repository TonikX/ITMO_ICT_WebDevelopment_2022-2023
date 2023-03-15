from http import client
import socket 

client = socket.socket()
client.connect(("127.0.0.1", 3300))

data = client.recv(1024)
print(data.decode('utf-8'))

client.close()