import socket 
import pickle

sock = socket.socket()
sock.connect(('127.0.0.1', 1337))

obj = {
	'top_side': input('Enter value of top side: '),
	'bot_side': input('Enter value of bot side: '),
	'perp': input('Enter value of perpendicular: ')
}

print('Send: ', obj)
data = pickle.dumps(obj)
sock.sendall(data)

msg = sock.recv(1024)
print('Answer: ', msg.decode('utf-8'))

print('Close')
sock.close()
