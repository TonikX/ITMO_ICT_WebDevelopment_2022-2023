import socket

udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_sock.sendto(b'Hello, server', ("localhost", 9090))

data, port_address = udp_sock.recvfrom(1024)
print(data.decode())

