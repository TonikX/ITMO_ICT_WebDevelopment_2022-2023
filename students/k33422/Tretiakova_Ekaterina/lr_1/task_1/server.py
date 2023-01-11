import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 14900))
sock.listen(2)

while True:
    try:
        con, addr = sock.accept()
        data = con.recv(16384)
        udata = data.decode("utf-8")
        print(udata)
        con.send(b"Hello, client")
    finally:
        sock.close()
        break