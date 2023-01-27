import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 10001))

cat = input("Введите длину 2 катетов для рассчета гипотенузы через пробел: ").encode('utf-8')
conn.send(cat)

data = conn.recv(4096)
c = data.decode('utf-8')
print(f'Длина гипотенузы: ' + c)

conn.close()


