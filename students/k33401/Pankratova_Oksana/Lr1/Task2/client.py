import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = input("Введите два основания и высоту через пробел: ")
msg = bytes(msg, 'utf-8')

s.connect((socket.gethostname(), 1234))
s.send(msg)
result = float(s.recv(1024).decode())
print("Площадь трапеции равна ", result)

s.close()
