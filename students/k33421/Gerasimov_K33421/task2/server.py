import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 9090))
sock.listen(1)

while True:
	try: 
		con, addr = sock.accept()
		s = con.recv(9111989)
		s = s.decode("utf8")
		s = s.split()
		a = int(s[0])
		b = int(s[1])
		h = int(s[2])
		con.send(b"S = " + str(0.5*h*(a+b)).encode("utf-8"))
	finally:
		sock.close()
		break