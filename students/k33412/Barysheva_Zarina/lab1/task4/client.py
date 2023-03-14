import socket
from threading import Thread


def listen_for_messages():
    while True:
        print(sock.recv(2048).decode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4851))

thread = Thread(target=listen_for_messages)
thread.daemon = True
thread.start()

while True:
    message_to_send = input()
    sock.send(message_to_send.encode("utf-8"))
    if message_to_send == '.q':
        sock.close()
        break