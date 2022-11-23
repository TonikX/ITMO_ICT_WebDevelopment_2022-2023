import socket

conn = socket.socket()
conn.bind(('localhost', 10801))
conn.listen(10)

while True:
    try:
        client_socket, addr = conn.accept()
        client_socket.recv(1024)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        with open("task3/index.html", "r") as f:
            body = f.read()
        res = response_type + headers + body
        client_socket.send(res.encode())
        client_socket.close()
    except KeyboardInterrupt:
        conn.close()
        break