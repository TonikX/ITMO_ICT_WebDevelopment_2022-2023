import socket

sock = socket.socket()
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

client, address = sock.accept()
msg = client.recv(1024)
print(msg.decode("utf-8"))
client.send(b"Hello, client!")
sock.close()