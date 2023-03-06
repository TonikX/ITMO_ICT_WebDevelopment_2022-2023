import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 2468))
server.listen()

while True:
    connection, address = server.accept()
    with open("index.html", 'r') as f:
        info = f.read()
    connection.sendto(f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{info}".encode("utf-8"), address)
    break

connection.close()