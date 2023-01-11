import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 14900))
sock.listen(2)

while True:
	try: 
		con, addr = sock.accept()
		s = con.recv(1024)
		s = s.decode("utf8")
		s = s.split()
		a = int(s[0])
		b = int(s[1])
		c = int(s[2])
		d = (pow(b, 2) - 4*a*c)
		if d == 0: 
			x = (-b/(2*a))
			con.send(b"x = " + str(x).encode("utf-8"))
		elif d < 0:
			con.send("Нет действительных корней".encode("utf-8"))
		elif d > 0:
			x1 = (- b - math.sqrt(d))/(2*a)
			x2 = (- b + math.sqrt(d))/(2*a)
			con.send(b"x1 = " + str(x1).encode("utf-8") + b" x2 = " + str(x2).encode("utf-8"))
	finally:
		sock.close()
		break