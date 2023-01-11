import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Поиск площади трапеции')
a = input('Введите длину верхнего основания: ')
b = input('Введите длину нижнего основания: ')
h = input('Введите длину высоты: ')

sock.send((a + ',' + b + ',' + h).encode())

data = sock.recv(1024)
sock.close()

print('Площадь трапеции равна: ', data.decode())