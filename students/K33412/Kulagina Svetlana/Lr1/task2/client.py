import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = input("Введите аргумент x^2:")
b = input("Введите аргумент x:")
c = input("Введите третий аргумент:")
s = a + " " + b + " " + c
sock.connect(("127.0.0.1", 14900))
sock.send(s.encode("utf-8"))
text=sock.recv(16384)
udata=text.decode("utf-8")
print(udata)