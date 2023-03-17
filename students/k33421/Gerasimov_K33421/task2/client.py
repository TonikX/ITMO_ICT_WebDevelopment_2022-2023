import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
a = input("Введите малое основание трапеции:")
b = input("Введите большое основание трапеции:")
h = input("Введите высоту трапеции:")
s = a + " " + b + " " + h
sock.connect(("127.0.0.1", 9090))
sock.send(s.encode("utf-8"))
text=sock.recv(9111989)
udata=text.decode("utf-8")
print(udata)