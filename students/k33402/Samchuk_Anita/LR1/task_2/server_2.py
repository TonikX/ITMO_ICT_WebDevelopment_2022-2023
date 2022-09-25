import socket
from math import sqrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    udata = data.decode('utf-8').split(',')
    for i in range(len(udata)):
        udata[i] = int(udata[i])

    if udata[0] == 1:
        c = sqrt(udata[1]**2 + udata[2]**2)
    else:
        c = sqrt(max(udata[1], udata[2])**2 - min(udata[1], udata[2])**2)
        if c == 0:
            c = 'Вы ввели неверные данные'
    conn.send(str(c).encode('utf-8'))

conn.close