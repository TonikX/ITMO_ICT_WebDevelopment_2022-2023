# -*- coding: utf-8 -*-

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 1337  # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print("Введите параметры a b h:")
params = input()
print(f'Sent {params}')
s.send(bytes(params, encoding='utf-8'))
ans = s.recv(1024)

s.close()

print(f"Received {ans.decode()}")
