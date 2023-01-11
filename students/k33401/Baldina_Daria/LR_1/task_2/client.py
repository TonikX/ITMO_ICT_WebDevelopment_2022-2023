import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
print('Введите коэффициенты квадратного уравнения')
a, b, c = map(int, input().split())
s.sendall((str(a)+','+str(b)+','+str(c)).encode('utf-8'))
answer = s.recv(1024)
print(answer.decode('utf-8'))
s.close()