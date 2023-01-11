import datetime
import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 9090
sock = socket.socket()
sock.connect((HOST, PORT))
print(f"Подключен к {HOST}:{PORT}")
name = input("Введите своё имя: ")

def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print("\n" + message)

thread = Thread(target=listen_for_messages)
thread.daemon = True
thread.start()

while True:
    text = input()
    if text.lower() == 'q':
        break
    date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    text = f'{date_now} {name} {text}'
    sock.send(text.encode())

sock.close()