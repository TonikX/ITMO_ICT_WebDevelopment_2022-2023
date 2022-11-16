import socket
import math
import pickle

conn = socket.socket()
conn.bind (("127.0.0.1", 3300))
conn.listen(1)

while True:
	try: 
		clientsocket, address = conn.accept()
		datz = clientsocket.recv(1024)
		numb = pickle.loads(datz)
		a = int(numb.get('a'))
		b = int(numb.get('b'))
		c = int(numb.get('c'))
		discr = b ** 2 - 4 * a * c
		if discr > 0: 
			x1 = (- b + math.sqrt(discr)) / (2 * a)
			x2 = (- b - math.sqrt(discr)) / (2 * a)
			clientsocket.send(b"x1 = " + (str(x1).encode("utf-8")) + b" x2 = " + (str(x2).encode("utf-8")))
		elif discr == 0:
			x = - b / (2 * a)
			clientsocket.send(b"x = " + (str(x).encode("utf-8")))
		else:
			clientsocket.send("Корней нет".encode("utf-8"))
	except KeyboardInterrupt:
		conn.close()
		break
