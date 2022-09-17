import socket
from math import sqrt

port = 3968
host = socket.gethostbyname("localhost")

#host="127.0.0.1"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #use TCP

sock.bind((host, port)) #связь сокета с хостом и портом
sock.listen(10) #n listenings 
cl_sock, addr = sock.accept() #приём и посылка данных
data=cl_sock.recv(1024)
print(data)
a, b,c = map(lambda x: int(x), data.split())

#conn.sendall('Wrong input format!\n'.encode())
D = b**2 - 4 * a * c
if D > 0:
    x1, x2 = (-b + sqrt(D)) / (2 * a), (-b - sqrt(D)) / (2 * a)
    cl_sock.sendall(f'Корни уравнения: {x1}, {x2}\n'.encode())
elif D == 0:
    x = (-b) / (2 * a)
    cl_sock.sendall(f'Корень уравнения: {x}\n'.encode())
else:
    cl_sock.sendall(f'Нет корней'.encode())

#message = bytes(mess, 'utf-8')

print(data.decode())
#cl_sock.send(message)

sock.close() #закрыли соединени