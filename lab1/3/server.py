import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))
    conn.listen(10)

    with open('index.html', 'r') as f:
        body = f.read()
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'

    response = response_type + headers + body

    print("HTTP server up and listening")
    while True:
        try:
            client_socket, addr = conn.accept()
            message = client_socket.recv(SOCKET_BUFF_SIZE)
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
        except:
            break
    conn.close()
