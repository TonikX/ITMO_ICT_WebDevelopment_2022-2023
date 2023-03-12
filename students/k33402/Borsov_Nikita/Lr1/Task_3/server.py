from socket import *
import pickle

host = 'localhost'
port = 777
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind(addr)
tcp_socket.listen()

print('Server was started!')

while True:
    conn, addr = tcp_socket.accept()
    print(f'client {addr} succesfully connected to our socket```')

    with open('index.html', 'r') as file:
        index_html_content = file.read()


    response = 'HTTP/1.0 200 OK\n\n' + index_html_content
    conn.send(response.encode())
    conn.close()

