import socket, sys
from threading import Thread


def send_message():
	while True:
		msg = input()
		s.send(msg.encode('utf-8'))
		if msg == "пока":
			s.close()
			break

def receive_message():
	while True:
		try:
			response = s.recv(16384)
			if response:
				print(response.decode('utf-8'))
		except OSError:	
			exit()

host = 'localhost'
port = 10015
s = socket.socket()
s.connect((host, port))

print("Вы подключались к чату. Введите 'пока', чтобы покинуть его.")
name = input("Введите Ваше имя: ")
s.send(name.encode('utf-8'))

sending = Thread(target = send_message)
receiving = Thread(target = receive_message)
sending.start()
receiving.start()
sending.join()
receiving.join()