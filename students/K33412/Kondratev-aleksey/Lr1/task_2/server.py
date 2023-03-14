import numbers
import socket, time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(1)
sock.setblocking(False)
print("Сервер запущен \nСервер ждет клиента")

while True:
	try:
		clientsocket, address = sock.accept()
		data = clientsocket.recv(16384)
		numbers = data.decode("utf-8")
		numbers = numbers.split()
		answer = int(numbers[0]) * int(numbers[1])
		answer = str(answer).encode('utf-8')
		clientsocket.send(answer)
		clientsocket.close()
		break
	except socket.error:
		print("Жду")
		time.sleep(3)
	except KeyboardInterrupt:
		clientsocket.close()
		break