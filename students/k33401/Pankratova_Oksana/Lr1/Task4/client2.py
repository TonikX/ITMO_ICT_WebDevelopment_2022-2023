import socket
import threading


def get_msg(sock):
    while True:
        msg = sock.recv(1024)
        print(msg.decode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 2022))
s.connect((socket.gethostname(), 2020))

get = threading.Thread(target=get_msg, args=(s,))
get.start()

while True:
    msg_send = input()
    s.send(bytes(msg_send, 'utf-8'))
