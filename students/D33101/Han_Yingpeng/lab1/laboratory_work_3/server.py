import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 4800))
server_socket.listen()

while True:
    client_connection, client_address = server_socket.accept()
    req = client_connection.recv(1024).decode()
    html_code = open('index.html')
    result = 'HTTP/1.0 200 OK\n\n' + html_code.read()
    html_code.close()
    if req == 'get adress':
        client_connection.send('http://127.0.0.1:4800'.encode())
    else:
        client_connection.sendall(result.encode())
    client_connection.close()