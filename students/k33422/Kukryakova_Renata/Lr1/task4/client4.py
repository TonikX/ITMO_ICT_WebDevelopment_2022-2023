import socket
import threading

conn = socket.socket()
conn.connect(('127.0.0.1', 8888))

username = input('Придумайте имя пользователя: ')


def receiver():
    while True:
        print(conn.recv(1024).decode())


def sender():
    while True:
        message = '{}: {}'.format(username, input(''))
        conn.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receiver)
receive_thread.start()

write_thread = threading.Thread(target=sender)
write_thread.start()

