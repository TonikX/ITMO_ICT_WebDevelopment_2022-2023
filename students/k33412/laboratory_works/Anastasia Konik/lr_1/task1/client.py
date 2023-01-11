import socket

# UDP client
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.connect(('localhost', 9090))
client_sock.sendto(b'Hello, server', ('localhost', 9090))
data, server = client_sock.recvfrom(1024)
client_sock.close()

print(data)
