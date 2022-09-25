import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(1)

clientsocket, address = server.accept()
data = clientsocket.recv(1024)
print(data.decode("utf-8"))
clientsocket.send("Hello, client!".encode("utf-8"))
clientsocket.close()
