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
		udata = data.decode("utf-8")
		print(udata)
		HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
		msg = 'Hello, client'.encode('utf-8')
		clientsocket.send(HDRS.encode('utf-8') + msg)
		sock.close()
		break
	except socket.error:
		print("Жду")
		time.sleep(3)
	except KeyboardInterrupt:
		sock.close()
		break