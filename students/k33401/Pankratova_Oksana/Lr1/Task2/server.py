# поиск площади трапеции

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clsocket, address = s.accept()
    a, b, h = clsocket.recv(1024).decode().split()
    S = str((float(a) + float(b)) / 2 * float(h))
    clsocket.send(bytes(S, 'utf-8'))
    clsocket.close()

