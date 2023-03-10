import socket
from math import sqrt

s = socket.socket()

s.bind(('127.0.0.1', 9090))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        print('Got empty data')
        break

    list_of_nums = data.decode('utf-8').split(',')

    d = float(list_of_nums[1]) ** 2 - 4 * float(list_of_nums[0]) * float(list_of_nums[2])

    if d > 0:
        result = f'Корни квадратного уравнения: {round((-float(list_of_nums[1]) + sqrt(d)) / (2 * float(list_of_nums[0])), 2)} {round((-float(list_of_nums[1]) + sqrt(d)) / (2 * float(list_of_nums[0])), 2)}'
        conn.send(result.encode('utf-8'))
    elif d == 0:
        result = f'Корень квадратного уравнения: {round(-float(list_of_nums[1]) / (2 * float(list_of_nums[0])), 2)}'
        conn.send(result.encode('utf-8'))
    else:
        conn.send('Дискриминант меньше 0. Решений нет'.encode('utf-8'))
conn.close()