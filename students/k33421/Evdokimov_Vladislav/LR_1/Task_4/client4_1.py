import socket
from threading import Thread


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def get(self):
        while True:
            try:
                data = self._socket.recv(1024)
                print(data.decode('utf-8'))
            except OSError:
                exit()

    def send(self):
        while True:
            message = input()
            if message == 'покинуть':
                self._socket.send(bytes(f'{message}', 'utf-8'))
                self._socket.close()
                break
            self._socket.send(bytes(f'{message}', 'utf-8'))


if __name__ == '__main__':
    clint = Client(53330)
    th_1, th_2 = Thread(target=clint.send), Thread(target=clint.get)
    th_1.start(), th_2.start()