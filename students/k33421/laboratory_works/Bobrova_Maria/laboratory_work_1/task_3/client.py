import socket

with socket.socket() as sock:
    sock.connect((socket.gethostname(), 1234))
    sock.settimeout(5)
    sock.send(b"GET / HTTP/1.1\n")
    data = sock.recv(16384)
    udata = data.decode('utf-8')
    print(udata)