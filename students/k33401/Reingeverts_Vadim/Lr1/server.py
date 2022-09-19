import socket

# UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Ensures that port is always ready to be used again
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 12346))

# Makes keyboard interrupt possible at all times
sock.settimeout(1.0)

while True:
    try:
        connection, client_address = None, None
        try:
            connection, client_address = sock.recvfrom(2048)
        except IOError:
            continue

        data = connection.decode('utf-8')
        print('Recived:', data)

        sock.sendto(b"Hello, client", client_address)

    except KeyboardInterrupt:
        print("Stopping server...")
        if connection:
            connection.close()
        break
sock.close()
