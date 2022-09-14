import math
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8091))
sock.listen(10)
client_socket, addr = sock.accept()
client_socket.send(b"Hello, client\nPlease enter the coefficients a, b, c of your equation like ax^2+bx+c=0")
coefs = client_socket.recv(1024).decode("utf-8")
'''
https://younglinux.info/python/task/quadratic
'''
a = float(coefs[0])
b = float(coefs[2])
c = float(coefs[4])
discr = b ** 2 - 4 * a * c

if discr < 0:
    msg = "No real roots"
elif discr == 0:
    x = -b / (2 * a)
    msg = "x = %.2f" % x
else:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    msg = "x1 = %.2f \nx2 = %.2f" % (x1, x2)

client_socket.send(msg.encode("utf-8"))
sock.close()
