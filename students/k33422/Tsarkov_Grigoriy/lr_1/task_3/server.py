import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    with open("index.html", "r") as f:
        index = f.read()
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'
    response = response_type + headers + index
    conn.send(response.encode("utf-8"))
    sock.close()
