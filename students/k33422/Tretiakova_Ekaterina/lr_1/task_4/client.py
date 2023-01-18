import socket
import random
from threading import Thread

host = "127.0.0.1"
port = 560
separator_token = " "
sock = socket.socket()
sock.connect((host, port))
print(f"Подключен к {host}:{port}")
name = input("Введите своё имя: ")

def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print("\n" + message)

thread = Thread(target=listen_for_messages)
#thread.daemon = True
thread.start()

while True:
    text = input()
    if text.lower() == 'exit':
        break
    text = f"{name}{separator_token}{text}"
    sock.send(text.encode())

sock.close()