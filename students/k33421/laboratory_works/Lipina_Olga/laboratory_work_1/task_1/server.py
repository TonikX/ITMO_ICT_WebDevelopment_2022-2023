import socket
udp_sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

udp_sock.bind(('', 9090))

# Listen for incoming datagrams
while (True):
    client_msg, address = udp_sock.recvfrom(1024)
    print(client_msg.decode())
    udp_sock.sendto(b"Hello, client", address)