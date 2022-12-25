import socket

conn = socket.socket()
conn.bind(('localhost', 9999))
conn.listen(1)

client, address = conn.accept()
msg = client.recv(1024)
print(msg.decode("utf-8"))
client.send(b"Hello, client!")
conn.close()