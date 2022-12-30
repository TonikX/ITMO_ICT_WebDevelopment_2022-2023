import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8080))
sock.listen(10)
while True:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    udata = data.decode("utf-8")
    print(udata)
    if not data:
        break
    conn.send(b"Hello, client! \n")
conn.close()