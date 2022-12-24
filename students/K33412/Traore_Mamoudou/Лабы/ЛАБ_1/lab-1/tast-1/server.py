import socket

host = '127.0.0.1'
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

clientsocket, address = sock.accept()
data = clientsocket.recv(16384)
udata = data.decode("utf-8")
print(udata)
clientsocket.send(b"Hello, client! \n")
sock.close()