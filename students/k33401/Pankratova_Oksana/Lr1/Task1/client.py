import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.connect((socket.gethostname(), 9090))


s.sendto(bytes('Hello, server', 'utf-8'), (socket.gethostname(), 9090))
msg = s.recvfrom(1024)
print(msg[0].decode())

s.close()
