import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('', 9090))
sock.send(b'Hello, server')

data = sock.recvfrom(1024)
sock.close

print(data[0].decode('utf-8'))
