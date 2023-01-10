import socket
from math import sqrt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    list_of_coef = data.decode('utf-8').split(',')
    for i in range(len(list_of_coef)):
        list_of_coef[i] = int(list_of_coef[i])
    #математические подсчеты
    d = list_of_coef[1]**2 - 4*list_of_coef[0]*list_of_coef[2]
    if d < 0:
        conn.sendall('Нет  решений'.encode('utf-8'))
    elif d == 0:
        result = 'Корень уравнения: ' + str(round(-list_of_coef[1]/(2*list_of_coef[0]),3))
        conn.sendall(result.encode('utf-8'))
    else:
        result = 'Корни квадратного уравнения: ' + str(round((-list_of_coef[1]-sqrt(d))/(2*list_of_coef[0]),3)) + ' ' + str(round((-list_of_coef[1]+sqrt(d))/(2*list_of_coef[0]),3))
        conn.sendall(result.encode('utf-8'))
conn.close()


