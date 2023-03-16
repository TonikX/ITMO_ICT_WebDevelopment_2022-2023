import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 62102))
server.listen(1)

while True:
    conn, addr = server.accept()

    page = open('index.html')
    content = page.read()
    page.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.sendall(response.encode())
    conn.close()
