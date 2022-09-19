import socket

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 12346))

sock.send(b"Hello, server")

data = sock.recv(2048)
data = data.decode('utf-8')
print('Recived:', data)

sock.close()
