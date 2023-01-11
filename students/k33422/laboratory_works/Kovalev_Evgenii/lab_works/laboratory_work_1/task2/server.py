import socket
from math import sqrt

s = socket.socket()

s.bind(('localhost', 9090))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    list_of_coef = data.decode('utf-8').split(',')

    discr = float(list_of_coef[1]) ** 2 - 4 * float(list_of_coef[0]) * float(list_of_coef[2])

    if discr > 0:
        result = 'Корни квадратного уравнения: ' + \
                 str(round((-float(list_of_coef[1]) + sqrt(discr)) / (2 * float(list_of_coef[0])), 2)) + ' ' + \
                 str(round((-float(list_of_coef[1]) - sqrt(discr)) / (2 * float(list_of_coef[0])), 2))
        conn.send(result.encode('utf-8'))
    elif discr == 0:
        result = 'Корень квадратного уравнения: ' + str(round(-float(list_of_coef[1]) / (2 * float(list_of_coef[0])), 2))
        conn.send(result.encode('utf-8'))
    else:
        conn.send('Дискриминант меньше 0. Нет решений'.encode('utf-8'))
conn.close()
