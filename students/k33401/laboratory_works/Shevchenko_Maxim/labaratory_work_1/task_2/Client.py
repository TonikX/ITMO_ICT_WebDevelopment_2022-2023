import socket 
import pickle

sock = socket.socket()
sock.connect(('', 7777))

cathetus = {
	'cathetus1': input('Enter value of first cathetus: '),
	'cathetus2': input('Enter value of second cathetus: ')
}

print('Send: ', cathetus)
data = pickle.dumps(cathetus)
sock.sendall(data)

msg = sock.recv(1024)
print('Answer: ', msg.decode('utf-8'))

print('Close')
sock.close()
