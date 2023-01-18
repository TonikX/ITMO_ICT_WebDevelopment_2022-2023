import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 6666))
sock.listen(1)

clientsocket, addr = sock.accept()
msg = clientsocket.recv(1024)
print(msg.decode("utf-8"))
clientsocket.send(bytes("Hello, client!!!!", "utf-8"))

clientsocket.close()
