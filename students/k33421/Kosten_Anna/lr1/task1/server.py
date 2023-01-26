import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8080))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall('Hello, client.'.encode('utf-8'))
    print(data.decode('utf-8'))
conn.close()