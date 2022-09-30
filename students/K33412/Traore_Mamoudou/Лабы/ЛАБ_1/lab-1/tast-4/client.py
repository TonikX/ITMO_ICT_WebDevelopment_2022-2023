import socket
import threading


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1', 8080
conn.connect(server)

username = input('Выберите псевдоним: ')


def recv_msg():
    while True:
        msg = conn.recv(2000).decode()
        if msg == 'username':
            conn.send(username.encode())
        else:
            print(msg)


def print_msg():
    while True:
        msg = '{} says: {}'.format(username, input(''))
        conn.send(msg.encode())


recv_thr = threading.Thread(target=recv_msg)
print_thr = threading.Thread(target=print_msg)
recv_thr.start()
print_thr.start()
