import socket

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
while True:
    connection, address = server.accept()
    page = open("index.html")
    info = page.read()
    page.close()
    data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + info
    connection.sendto(data.encode("utf-8"), address)
    print("Client receive the information")
    break

connection.close()

