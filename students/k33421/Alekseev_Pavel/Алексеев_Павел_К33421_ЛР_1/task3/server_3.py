import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7171))
sock.listen(10)
sock, addr = sock.accept()

file = open('index.html', 'r')

ht = 'HTTP/1.0 200 OK\n' + file.read()
sock.sendall(ht.encode("utf-8"))

file.close()
sock.close()
