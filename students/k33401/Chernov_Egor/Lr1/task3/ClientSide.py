import socket


with socket.socket() as s:
    s.connect(('127.0.0.1', 8080))
    s.settimeout(5)
    s.send(b"GET / HTTP/1.1\n")
    data = s.recv(16384)
    decodeData = data.decode('utf-8')
    print(decodeData)
