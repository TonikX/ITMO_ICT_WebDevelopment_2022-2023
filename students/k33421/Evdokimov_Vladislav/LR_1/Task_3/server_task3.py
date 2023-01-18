import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 6060))
sock.listen(1)

conn, addr = sock.accept()
conn.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open("index.html", "rb").read())

conn.close()


