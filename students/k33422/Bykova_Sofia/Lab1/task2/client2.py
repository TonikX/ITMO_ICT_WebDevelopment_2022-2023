import socket

sock_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_cli.connect(('localhost', 9090))

h = input("Введите значения высоты и основания параллелограмма -> ")
sock_cli.send(bytes(h.encode('utf-8')))

data = sock_cli.recv(4096)
data = data.decode('utf-8')

print(f'Площадь = {data}')
