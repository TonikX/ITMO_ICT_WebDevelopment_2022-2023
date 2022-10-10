import socket

conn = socket.socket()
conn.bind (("127.0.0.1", 3300))
conn.listen(1)

clientsocket, address = conn.accept()
data = clientsocket.recv(1024)
print(data.decode("utf-8"))

clientsocket.send("Hello, client".encode("utf-8"))

clientsocket.close()