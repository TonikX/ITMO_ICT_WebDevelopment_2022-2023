import socket

host = 'localhost'
port = 5002
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(10)


while True:
    conn, address = sock.accept()
    response_type = "/HTTP/1.0 200 OK\n"
    headers = "Content-Type: text/html\n\n"
    file = open('index.html', 'r')
    body = file.read()
    response = response_type + headers + body
    conn.sendall(response.encode('utf-8'))
    conn.close()


