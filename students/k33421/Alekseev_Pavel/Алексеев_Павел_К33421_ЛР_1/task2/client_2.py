import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8001))

mess = input("Введите длину 2 катетов (через пробел) для рассчета гипотенузы : ").encode('utf-8')
sock.send(mess)

data = sock.recv(4096)
res = data.decode('utf-8')
print(f'Длина гипотенузы: ' + res)

sock.close()