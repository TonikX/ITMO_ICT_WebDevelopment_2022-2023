import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    fin = open('index.html')
    content = fin.read()
    fin.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.send(response.encode())

    conn.close()