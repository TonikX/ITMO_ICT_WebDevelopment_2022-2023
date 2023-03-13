import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5678))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    server_file = open('index.html', 'rb')

    client_socket.sendfile(server_file)
