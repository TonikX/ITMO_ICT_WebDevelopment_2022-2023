Лабораторная работа №1 - Работа с сокетами
Цель: Овладеть практическими навыками и умениями реализации web-серверов и использования сокетов.
Практическое задание:
Задание №1:
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента. Обязательно использовать библиотеку socket.


client.py:
import socket

conn = socket.socket()
conn.connect(('localhost', 9999))

conn.send(b'Hello server! \n')

data = conn.recv(1024)
print(data.decode("utf-8"))

conn.close()


server.py:
import socket

conn = socket.socket()
conn.bind(('localhost', 9999))
conn.listen(1)

client, address = conn.accept()
msg = client.recv(1024)
print(msg.decode("utf-8"))
client.send(b"Hello, client!")
conn.close()


Задание №2:
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера решение теоремы Пифагора. Сервер обрабатывает полученные данные и возвращает результат клиенту. Обязательно использовать библиотеку socket. (5 вариант в журнале)


client.py:
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(('localhost', 10001))

cat = input("Введите длину 2 катетов для рассчета гипотенузы через пробел: ").encode('utf-8')
conn.send(cat)

data = conn.recv(4096)
c = data.decode('utf-8')
print(f'Длина гипотенузы: ' + c)

conn.close()


server.py:
import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 10001))
conn.listen(10)
conn, addr = conn.accept()

data_from_client = conn.recv(5096)
cat = data_from_client.decode("utf-8")

r = cat.split()
a = float(r[0])
b = float(r[1])
c = round(math.sqrt(a**2 + b**2), 3)

conn.send(str(c).encode("utf-8"))

conn.close()


Задание №3:
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html. Обязательно использовать библиотеку socket.

server.py:
import socket

conn = socket.socket()
conn.bind(('localhost', 10801))
conn.listen(10)

while True:
    try:
        client_socket, addr = conn.accept()
        client_socket.recv(1024)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        with open("index.html", "r") as f:
            body = f.read()
        res = response_type + headers + body
        client_socket.send(res.encode())
        client_socket.close()
    except KeyboardInterrupt:
        conn.close()
        break


index.html:
<!DOCTYPE html>
<html>
    <head>
        <title>Ссылка!</title>
    </head>
    <body>

    <a href="https://github.com">Visit Github!</a>

    </body>
</html>


Задание №4:
Реализовать двухпользовательский или многопользовательский чат. Реализация многопользовательского часа позволяет получить максимальное количество баллов. Обязательно использовать библиотеку threading.


client.py:
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


server.py:
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


Задание №5:
Написать простой web-сервер для обработки GET и POST http запросов средствами Python и библиотеки socket, который может: принять и записать информацию о дисциплине и оценке по дисциплине, отдать информацию обо всех оценках по дисциплине в виде html-страницы.

server.py:
import socket
import sys

MAX_LINE = 64 * 1024


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._subjects = []
        self._marks = []

    def serve_forever(self):
        conn = socket.socket()

        try:
            conn.bind((self._host, self._port))
            conn.listen()

            while True:
                conn, _ = conn.accept()
                try:
                    self.serve_client(conn)
                except Exception:
                    print('Client serving failed', Exception)
        finally:
            conn.close()

    def serve_client(self, conn):
        data = conn.recv(16384).decode('utf8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp is not None:
            self.send_response(conn, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as f:
                    resp += f.read()
                return resp

            if method == 'POST':
                resp = "HTTP/1.1 204 OK\n\n"

                params = body.split('&')
                for a in params:
                    if a.split('=')[0] == 'subj':
                        self._subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        self._marks.append(a.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, m in zip(self._subjects, self._marks):
                    resp += f"<li>Subject: {s}, Grade: {m}</li>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf8'))


if __name__ == '__main__':
    host ='localhost'
    port = 8765

    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass


index.html:
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Journal</title>
</head>
<body>
<form action="/" method="post">
        <label for="subject">Subject:</label>
        <input type="text" name="subject" id="subject"/>
        <label for="grade">Grade:</label>
        <input type="number" name="grade" id="grade"/>
        <button>Update_journal</button>
</form>
</body>
</html>

