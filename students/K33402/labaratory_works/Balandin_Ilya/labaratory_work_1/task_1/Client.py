import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 1337))

sock.send(b'Hello, I am CLient \n')