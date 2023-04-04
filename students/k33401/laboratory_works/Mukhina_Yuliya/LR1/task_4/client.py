import socket
from threading import Thread

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
client.connect(('127.0.0.1', 9090))

def listen():
    while True:
        data = client.recv(2048)
        print(data.decode('utf-8'))

def send():
    lis_thread = Thread(target=listen) #слушаем в потоке
    lis_thread.start()
    while True:
        client.send((nick + ': ' + input()).encode('utf-8'))

if __name__== '__main__':
    nick = input('Введите ник: ')
    send()