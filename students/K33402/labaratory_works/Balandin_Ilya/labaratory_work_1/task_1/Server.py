import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 1337))

data = sock.recv(1024)
udata = data.decode('utf-8')

print(f'Client message: {udata}')
sock.close()

