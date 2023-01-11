import socket

sock = socket.socket()
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

client, address = sock.accept()
client.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open('index.html', 'rb').read())
msg = client.recv(1024)

client.close()