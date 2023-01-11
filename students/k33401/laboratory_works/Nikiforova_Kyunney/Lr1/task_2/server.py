import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode()
    data = data.split(',')
    a = data[0]
    b = data[1]
    h = data[2]

    S = 0.5 * (int(a) + int(b)) * int(h)
    print(S)

    conn.send(str(S).encode())

conn.close()