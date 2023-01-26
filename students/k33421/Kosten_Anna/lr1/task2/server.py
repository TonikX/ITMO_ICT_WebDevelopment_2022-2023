from math import sqrt
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    coefs = data.decode('utf-8').split(',')
    for i in range(len(coefs)):
        coefs[i] = int(coefs[i])

    d = coefs[1]**2 - 4*coefs[0]*coefs[2]
    if d < 0:
        conn.sendall('No solutions'.encode('utf-8'))
    elif d == 0:
        result = 'Equations`s roots: ' + str(round(-coefs[1]/(2*coefs[0]),3))
        conn.sendall(result.encode('utf-8'))
    else:
        result = 'Quadratic equations`s roots: ' + str(round((-coefs[1]-sqrt(d))/(2*coefs[0]),3)) + ' ' + str(round((-coefs[1]+sqrt(d))/(2*coefs[0]),3))
        conn.sendall(result.encode('utf-8'))
conn.close()