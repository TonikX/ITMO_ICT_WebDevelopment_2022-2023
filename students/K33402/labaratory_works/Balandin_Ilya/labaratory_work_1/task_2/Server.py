import socket
import pickle

def trapezoidSquare(data):
	obj = pickle.loads(data)
	top_side = int(obj.get('top_side'))
	bot_side = int(obj.get('bot_side'))
	perp = int(obj.get('perp'))
	return ((top_side + bot_side) / 2) * perp

sock = socket.socket()
sock.bind(('127.0.0.1', 1337))
sock.listen(1)

conn, addr = sock.accept()

all_data = bytearray()

while True:
	data = conn.recv(1024)
	if not data:
		break
	all_data += data

	result = trapezoidSquare(all_data)
	result = str(result)
	conn.send(result.encode('utf-8'))

print('Close')
conn.close