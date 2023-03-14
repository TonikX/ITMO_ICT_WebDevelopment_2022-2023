import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4467))
sock.listen(1)
conn, addr = sock.accept()

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        with open('index.html', "r") as file:
            html = file.read()
        conn.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode())
