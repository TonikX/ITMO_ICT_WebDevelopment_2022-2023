import socket
import pickle
import math

def pythagoras(data):
	obj = pickle.loads(data)
	cathetus1 = int(obj.get('cathetus1'))
	cathetus2 = int(obj.get('cathetus2'))
	return math.sqrt(cathetus1*cathetus1 + cathetus2*cathetus2)

sock = socket.socket()
sock.bind(('127.0.0.1', 7777))
sock.listen(1)

conn, addr = sock.accept()

all_data = bytearray()

while True:
	data = conn.recv(1024)
	if not data:
		break
	all_data += data

	hypotenuse = pythagoras(all_data)
	hypotenuse = str(hypotenuse)
	conn.send(hypotenuse.encode('utf-8'))

print('Close')
conn.close
