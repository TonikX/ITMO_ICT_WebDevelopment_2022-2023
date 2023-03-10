import socket

s = socket.socket()
s.connect(('localhost', 9090))

a, b, c = map(float, input('Введите коэффициенты квадратного уравнения').split())
s.send(','.join([str(a), str(b), str(c)]).encode('utf-8'))

answer = s.recv(1024)
print(answer.decode('utf-8'))

s.close()