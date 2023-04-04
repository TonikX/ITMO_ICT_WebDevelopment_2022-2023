import socket

sock = socket.socket()

sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()


while True:
    data = conn.recv(1024)
    udata = data.decode("utf-8")
    
    if not data:
        break
    print(udata)
    conn.send(b'Hello, client')
    
conn.close()