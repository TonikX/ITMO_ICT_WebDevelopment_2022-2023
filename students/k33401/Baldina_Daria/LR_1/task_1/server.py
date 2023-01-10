import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8080)) # привязываем сокет к localhost и 8080 порту.
s.listen(1) # начинаем прослушивать входящие соединения
conn, addr = s.accept() # метод, который принимает входящее соединение(ждет подключения)

while True:
	data = conn.recv(1024) #получаем данные из сокета.
	if not data:
		break
	conn.sendall('Hello, client.'.encode('utf-8')) #отправляем сообщение для клиента в сокет.
	print(data.decode('utf-8'))
conn.close()
