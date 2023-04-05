import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1212))
s.listen(5)

while True:
    clsocket, addr = s.accept()
    clsocket.send(bytes('HTTP/1.1 200 OK\n', 'utf-8'))
    clsocket.send(bytes('Content-Type: text/html; charset=utf-8\n', 'utf-8'))
    clsocket.send(bytes('Content-Length: 144\n', 'utf-8'))
    clsocket.send(bytes('\n', 'utf-8'))
    clsocket.send(bytes('\n', 'utf-8'))

    file = open('index.html', 'rb')

    for line in file:
        clsocket.send(line)
    clsocket.close()

s.close()
