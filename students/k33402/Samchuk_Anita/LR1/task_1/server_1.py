import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9090))

while True:
    conn, addr = sock.recvfrom(1024)
    print('client addr: ', addr)

    sock.sendto(b'Hello, client', addr)

sock.close

