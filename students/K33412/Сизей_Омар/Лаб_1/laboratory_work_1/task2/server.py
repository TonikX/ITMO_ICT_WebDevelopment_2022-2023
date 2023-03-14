import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

#Version with trapezoid

clientsocket, address = sock.accept()
clientsocket.send(b"Enter large trapezoid base:")
data = clientsocket.recv(16384)
large_base = int(data.decode())
clientsocket.send(b"Enter small trapezoid base:")
data = clientsocket.recv(16384)
small_base = int(data.decode())
clientsocket.send(b"Enter trapezoid height:")
data = clientsocket.recv(16384)
height = int(data.decode())
area = height * ((large_base + small_base) / 2)
clientsocket.send(f"Trapezoid area: {area}".encode())
sock.close()