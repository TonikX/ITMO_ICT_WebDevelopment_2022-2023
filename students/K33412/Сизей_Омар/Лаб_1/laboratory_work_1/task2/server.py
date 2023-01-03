import socket


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 14900))
sock.listen(10)

# Version with parallelogram

clientsocket, address = sock.accept()
clientsocket.send(b"Enter parallelogram base:")
data = clientsocket.recv(1024)
large_base = int(data.decode())
clientsocket.send(b"Enter parallelogram height:")
data = clientsocket.recv(1024)
height = int(data.decode())
area = height * large_base
clientsocket.send(f"parallelogram area: {area}".encode())
sock.close()
