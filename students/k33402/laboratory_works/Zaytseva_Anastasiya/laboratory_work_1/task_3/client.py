import socket

LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket()
sock.connect(('localhost', LOCAL_PORT))

data = sock.recv(BUFFER_SIZE)
print(data.decode('utf-8'))

sock.close()
