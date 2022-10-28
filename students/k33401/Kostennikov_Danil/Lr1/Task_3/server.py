
import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    html_file = open('index.html', 'r').read()
    cliensocket.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html_file}'.encode())
    cliensocket.close()