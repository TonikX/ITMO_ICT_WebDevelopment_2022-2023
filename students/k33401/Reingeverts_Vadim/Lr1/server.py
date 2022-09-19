import socket

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 12346))

while True:
    try:
        data, client_address = sock.recvfrom(2048)
        data = data.decode('utf-8')
        print('Recived:', data)

        sock.sendto(b"Hello, client", client_address)
    except KeyboardInterrupt:
        print("Stopping server...")
        sock.close()
        break
