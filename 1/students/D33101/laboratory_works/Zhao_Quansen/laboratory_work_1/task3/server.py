import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 4245))
server_socket.listen()

while True:
    client, address = server_socket.accept()
    req = client.recv(1024).decode()
    code = open('index.html')
    res = 'HTTP/1.0 200 OK\n\n' + code.read()
    code.close()
    if req == 'адрес страницы':
        client.send(f'Адрес страницы: http://127.0.0.1:4245'.encode())
    else:
        client.sendall(res.encode())
    client.close()
