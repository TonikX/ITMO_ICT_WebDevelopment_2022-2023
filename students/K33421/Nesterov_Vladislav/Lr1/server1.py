# -*- coding: utf-8 -*-

import socket

sock = socket.socket()

sock.bind(('', 1337))  # номер открытого порта
sock.listen(1)  # размер очереди прослушивания
conn, addr = sock.accept()  # объявляем начало приёма данных от клиента с адресом addr на сокете conn

while True:
    data = conn.recv(1024).decode()  # получение данных пакетами по 1024 байта
    print(data)
    if not data:
        break
    conn.send('Hello, client'.encode())

conn.close()
