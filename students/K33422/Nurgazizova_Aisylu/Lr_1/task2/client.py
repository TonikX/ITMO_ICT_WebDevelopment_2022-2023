import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 8080))
a = input("Введите высоту: ")
b = input("Введите основание: ")
conn.send(a.encode())
conn.send(b.encode())
c_bin = conn.recv(2000)
c = c_bin.decode('utf-8')
print('Площадь параллелограмма: ', c)
conn.close()
