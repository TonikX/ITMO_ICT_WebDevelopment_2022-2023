from socket import *

tcp_socket = socket(AF_INET,SOCK_STREAM)
tcp_socket.connect(('127.0.0.1', 4800))

print('<--Pythagorean theorem-->')
a = float(input('The first side of the triangle: '))
b = float(input('The second side of the triangle: '))
tcp_socket.send(f'{a},{b}'.encode())

solution = tcp_socket.recv(1024)
print(f'Solution: \n{solution.decode()}')

tcp_socket.close()