import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5675))
sock.listen(1)
conn, addr = sock.accept()

while True:
    conn.send("Enter figure's base and height lengths in form like x, y:".encode('utf-8'))
    try:
        data = conn.recv(1024)
        a, h = data.decode('utf-8').split(', ')
        s = (int(a) * int(h))
        print('Area is', s)
    except KeyboardInterrupt:
        conn.close()
        break
sock.close()


