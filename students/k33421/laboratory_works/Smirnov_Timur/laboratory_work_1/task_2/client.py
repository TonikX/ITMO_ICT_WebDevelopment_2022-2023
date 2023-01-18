import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

data = sock.recv(1024).decode('utf-8')
print(data)
base = input('>>')
sock.send(base.encode('utf-8'))

data = sock.recv(1024).decode('utf-8')
print(data)
height = input('>>')
sock.send(height.encode('utf-8'))

data = sock.recv(1024).decode('utf-8')
print(data)

input('Push ENTER to exit >>')
