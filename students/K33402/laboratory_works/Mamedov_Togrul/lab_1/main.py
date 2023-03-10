import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send('Hello, client'.encode('utf-8'))
    print(data.decode('utf-8'))
conn.close()