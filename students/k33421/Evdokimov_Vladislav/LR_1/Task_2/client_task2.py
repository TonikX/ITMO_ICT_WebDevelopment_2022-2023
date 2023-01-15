import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5675))

while True:
    try:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        sock.send(input().encode('utf-8'))
    except KeyboardInterrupt:
        sock.close()
        break

sock.close()




