import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 8901))
conn.listen(10)

while True:
    try:
        client_socket, addr = conn.accept()
        client_socket.recv(1024)
        # Set appropriate headers
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        # Read HTML from file
        with open("index.html", "r") as f:
            body = f.read()
        res = response_type + headers + body
        client_socket.send(res.encode())
        client_socket.close()
    except KeyboardInterrupt:
        conn.close()
        break
