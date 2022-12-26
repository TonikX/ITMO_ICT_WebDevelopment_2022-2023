# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

sock.connect(('localhost', 1337))
sock.send('Hello, server'.encode())

data = sock.recv(1024)
sock.close()

print(data.decode())
