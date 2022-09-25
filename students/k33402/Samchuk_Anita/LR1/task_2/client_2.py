import socket

sock = socket.socket()
sock.connect(('', 8080))

print('Что вам надо посчитать?\n1)Гипотенуза\n2)Катет')
answer = input()
print('Введите известные стороны')
a, b = map(int, input().split())
sock.send('{},{},{}'.format(answer, a, b).encode('utf-8'))

data = sock.recv(1024)
sock.close

print(data.decode('utf-8'))
