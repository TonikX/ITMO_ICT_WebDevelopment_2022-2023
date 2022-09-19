import socket

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 12346))

sock.send(b"Hello, server")

try:
    connection = sock.recv(2048)
    data = connection.decode('utf-8')
    print('Recived:', data)
except ConnectionResetError:
    print("Could not connect to the server")

sock.close()
