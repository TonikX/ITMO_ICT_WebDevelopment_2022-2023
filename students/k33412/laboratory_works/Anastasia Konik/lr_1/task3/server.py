import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 8080))
server_sock.listen(5)

while True:
    client_sock, client_addr = server_sock.accept()
    data = client_sock.recv(1024)
    if not data:
        break
    status_line = "HTTP/1.0 200 OK\n"
    resp_headers = "Content-Type: text/html\n\n"
    body = open('index.html', 'r').read()
    response = status_line + resp_headers + body
    client_sock.sendall(response.encode("utf-8"))
    open('index.html', 'r').close()
    client_sock.close()
