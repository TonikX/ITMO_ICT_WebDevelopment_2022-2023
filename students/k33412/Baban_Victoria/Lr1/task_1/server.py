import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    conn.send(b'Hello, client.\n')

conn.close()