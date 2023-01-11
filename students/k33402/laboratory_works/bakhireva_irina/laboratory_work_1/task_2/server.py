import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

while True:
    client, address = sock.accept()
    s = int(client.recv(1024).decode())
    h = int(client.recv(1024).decode())
    result = str(s*h)
    client.send(result.encode())
