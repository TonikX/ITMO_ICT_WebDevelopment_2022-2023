import socket

sock = socket.socket()
sock.bind( ('', 9090) )
sock.listen(10)
conn, addr = sock.accept()

while True:
    data = conn.recv(16384)
    if not data:
        break
    conn.send(b'Hello, client')

conn.close

