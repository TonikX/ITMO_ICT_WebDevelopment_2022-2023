import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('localhost', 12346))

sock.listen(10)

while True:
    try:
        client_sock, address = sock.accept()

        data = client_sock.recv(10240)
        data = data.decode('utf-8')
        print('Recived:', data)

        client_sock.send(b"Hello, client")
    except KeyboardInterrupt:
        print("Stopping server...")
        sock.close()
        break
