from socket import *

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

print("Решение квадратного уравнения.")
print("Введите коэффициенты для уравнения: ax^2 + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
socket.send(f'{a},{b},{c}'.encode())
recv_data = socket.recv(1024)
print(f'Решение: \n{recv_data.decode()}')

socket.close()