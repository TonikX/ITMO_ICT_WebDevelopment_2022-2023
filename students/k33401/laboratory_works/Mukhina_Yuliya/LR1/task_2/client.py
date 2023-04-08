import socket
import numpy as np
import pickle

sock = socket.socket()
sock.connect(('localhost', 9090))

obj = {
    'a': input('Введите первую сторону: '),
    'b': input('Введите вторую сторону: '),
    'gr': input('Введите угол между сторонами: ')
}

data = pickle.dumps(obj)
if data:
    sock.send(data)

data = sock.recv(1024)
udata = data.decode("utf-8")
print (udata)

sock.close()