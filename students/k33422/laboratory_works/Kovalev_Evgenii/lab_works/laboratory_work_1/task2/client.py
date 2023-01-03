import socket

s = socket.socket()
s.connect(('localhost', 9090))

print('Введите коэффициенты квадратного уравнения')

a, b, c = map(float, input().split())
s.send((str(a) + ',' + str(b) + ',' + str(c)).encode('utf-8'))

answer = s.recv(1024)
print(answer.decode('utf-8'))

s.close()