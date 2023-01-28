import socket

# UDP server
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(('localhost', 9090))

while True:
    data, address = server_sock.recvfrom(1024)
    if data == b'Hello, server':
        print(data)
        server_sock.sendto(b'Hello, client', address)
    else:
        server_sock.close()
        break
