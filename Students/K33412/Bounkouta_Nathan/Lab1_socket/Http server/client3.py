import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.1.5'
port = 8000
server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()

    page = open('index.html')
    content = page.read()
    page.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.sendall(response.encode())
    conn.close()