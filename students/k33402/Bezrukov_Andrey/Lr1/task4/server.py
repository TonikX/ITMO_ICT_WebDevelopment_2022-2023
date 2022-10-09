import socket, threading


def chat_client(name, client_sock, clients):
	while True:
		try:
			message = client_sock.recv(16384)
			if message.decode('utf-8') == "пока":
				client_sock.close()
				delete_client_sock(client_sock, clients)
				for client in clients:
					client[1].send(name + ' покинул(а) чат')
			else:
				for client in clients:
					if (client[1]!=client_sock):
						client[1].send(name + b' > ' + message)
		except OSError:
			pass


def delete_client_sock(client_sock, clients):
	for client in clients:
		if client[1] == client_sock:
			clients.remove(client)
			break


if __name__ == '__main__':
	host = 'localhost'
	port = 10015
	s = socket.socket()
	s.bind((host, port))

	clients = []

	while True:
		try:
			s.listen()
			client_sock, client_addr = s.accept()
			name = client_sock.recv(1024)
			print("Подключенный клиент:", client_addr)

			clients.append((name, client_sock))

			for client in clients:
				if client[1]!=client_sock:
					client[1].send(name + 'вошел(ла) в чат')

			client_thread = threading.Thread(target = chat_client, args= (name, client_sock, clients))
			client_thread.start()


		except KeyboardInterrupt:
			s.close()
			break