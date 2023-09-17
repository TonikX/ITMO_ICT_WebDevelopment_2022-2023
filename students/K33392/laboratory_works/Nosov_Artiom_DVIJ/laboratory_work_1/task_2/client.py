import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

msg = input("Введите основание и высоту параллелограмма через пробел: ")
msg = bytes(msg, 'utf-8')

s.connect((socket.gethostname(), 7070))
s.send(msg)
result = float(s.recv(1000).decode())
print("Площадь параллелограмма равна ", result)

s.close()