# -*- coding: utf-8 -*-
"""
Поиск площади трапеции

S_trap = (a+b)*h/2, где a, b - основания
"""

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 1337  # Port to listen on (non-privileged ports are > 1023)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
while True:
    conn, addr = s.accept()
    print(f"Connection from {addr} is now established")
    params = conn.recv(1024)
    print(f"Получил параметры {params.decode()}, вычисляю...")
    a, b, h = params.decode().split()
    a, b, h = int(a), int(b), int(h)
    S_trap = float((a + b) * h / 2)
    print(f"Ответ: {S_trap}")
    conn.send(f"Площадь трапеции с введенными параметрами = {S_trap}".encode())
    print("Работу выполнил, отключаюсь...")
    break
conn.close()
