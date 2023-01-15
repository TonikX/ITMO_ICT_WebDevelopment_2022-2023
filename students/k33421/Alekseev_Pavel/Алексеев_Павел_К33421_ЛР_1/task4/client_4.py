import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1', 8080
sock.connect(server)

name = input('Выберите псевдоним: ')

def sms_write():
    while True:
        sms = name + ' написал: {}'.format(input(''))
        sock.send(sms.encode())

def sms_recive():
    while True:
        sms = sock.recv(2000).decode()
        if sms == 'username':
            sock.send(name.encode())
        else:
            print(sms)

recive_thr = threading.Thread(target=sms_recive)
write_thr = threading.Thread(target=sms_write)

recive_thr.start()
write_thr.start()