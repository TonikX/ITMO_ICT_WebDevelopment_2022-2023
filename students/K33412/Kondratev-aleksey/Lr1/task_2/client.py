import socket

str = input("Введите сторону и высоту параллелограмма: ")
str = str.encode('utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
sock.send(str)
data = sock.recv(16384)
res = data.decode('utf-8')
print(f'Площадь параллелограмма {res}')
sock.close()