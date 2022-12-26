import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s1.sendto(str.encode('Hello, server!'), ('localhost', 9090))
msg = s1.recvfrom(1024)
msgg = 'Message from server: {}'.format(msg[0].decode('utf-8'))
print(msgg)