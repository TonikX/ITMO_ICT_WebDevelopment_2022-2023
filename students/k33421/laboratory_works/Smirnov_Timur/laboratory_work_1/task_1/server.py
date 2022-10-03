import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
print(data.decode('utf-8'))

msg = 'Hello, client!'
conn.send(msg.encode('utf-8'))

conn.close()
