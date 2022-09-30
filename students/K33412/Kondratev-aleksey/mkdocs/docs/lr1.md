# Лабораторная работа №1

## Задача №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

* `server.py`

Сервер, который ждет подключение клиента, чтобы отправить ему привет

```python
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
```

* `client.py`

Клиент, который подключается к серверу, чтобы отправить ему привет

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
sock.send(b"Hello, server\n")
data = sock.recv(16384)
res = data.decode('utf-8')
print(res)
sock.close()
```

## Задача №2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Поиск площади параллелограмма

* `server.py`

Серверная часть, которая получает данные и с помощью них совераеш подсчет и отправляет назад конечное значение

```python
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
```

* `client.py`

Клиент говорит с помощью каких чисел нужно посчитать нашу площадь

```python
import socket

str = input("Введите сторону и высоту параллелограмма: ")
str = str.encode('utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9090))
sock.send(str)
data = sock.recv(16384)
res = data.decode('utf-8')
print(f'Площадь параллелограмма {res}')
sock.close()
```

## Задача №3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

* `server.py`

Серверно условно получает GET запрос и отправляет на него нашу страничку которая лежит на сервере

```python
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9090
sock.bind((host, port))
sock.setblocking(False)

print("Сервер запущен", host, port)

sock.listen(3)

while True:
    try:
        clientsocket, (client_host, client_port) = sock.accept()
        print('Got connection from', client_host, client_port)
        data = clientsocket.recv(16384)
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        body = """
            <html>
            <body>
            <h1>Hello world!</h1>
            </body>
            </html>
        """
        response = HDRS + body
        clientsocket.send(response.encode('utf-8'))
        clientsocket.close()
        break
    except socket.error:
        print("Жду")
        time.sleep(3)
    except KeyboardInterrupt:
        clientsocket.close()
```

## Задача №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

* `server.py`

Сервеная часть задания, где мы обрабатываем сообщения одного пользователя, а после рассылаем отправленное сообщение каждому

```python
import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 9090
clients = []
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)
print(f"Сервер запущен {HOST}:{PORT}")

def listen_for_client(people):
    while True:
        try:
            message = people.recv(1024).decode()
        except Exception as e:
            print(f"[!] Ошибка: {e}")
            clients.pop(people)
        else:
            message = message.replace(" ", ": ")
        for client in clients:
            client.send(message.encode())

while True:
    client, (port, host) = sock.accept()
    print(f"подключен {port}:{host}.")
    clients.append(client)
    thread = Thread(target=listen_for_client, args=(client,))
    thread.daemon = True
    thread.start()
```

* `client.py`

Клиентская часть, где мы подключаемся к серверу и отправляем сообщения на него, чтобы уже тот разослал его другим пользователям

```python
import datetime
import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 9090
sock = socket.socket()
sock.connect((HOST, PORT))
print(f"Подключен к {HOST}:{PORT}")
name = input("Введите своё имя: ")

def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print("\n" + message)

thread = Thread(target=listen_for_messages)
thread.daemon = True
thread.start()

while True:
    text = input()
    if text.lower() == 'q':
        break
    date_now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    text = f'{date_now} {name} {text}'
    sock.send(text.encode())

sock.close()
```

## Задача №5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:

Принять и записать информацию о дисциплине и оценке по дисциплине.

Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

* `server.py`

Сервер, который реализует запись в локальную "базу данных", которая работает пока 
запущен сервер и в последствие ее вывод, чтобы пользователь мог понять какие оценки были уже записаны

```python
import socket

class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        while True:
            clientsocket, _ = sock.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(16384)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, target, protocol = lines[0].split()
        return target, method

    def parse_headers(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        i = lines.index('')
        headers = lines[1:i]
        body = lines[-1]
        return headers, body

    def handle_request(self, target, method, body):
        if target == "/":
            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

            if method == "POST":
                newbody = body.split('&')
                for a in newbody:
                    if a.split('=')[0] == 'subject':
                        subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        marks.append(a.split('=')[1])

                resp = "HTTP/1.1 200 OK\n\n"
                resp += "<html><head><title>Journal</title></head><body>"
                for s, m in zip(subjects, marks):
                    resp += f"<p>{s}: {m}</p>"
                resp += "</body></html>"
                return resp

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))

if __name__ == '__main__':
    host = 'localhost'
    port = 9090
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

* `index.html`

Простой HTML для отправки оценки по какому-то предмету 

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Journal</title>
</head>
<body>
<form action="/" method="post">
    <div>
        <label for="name">Subject:</label>
        <input type="text" id="name" name="subject"/>
    </div>
    <div>
        <label for="mail">Mark:</label>
        <input type="number" id="mail" name="mark"/>
    </div>
    <div>
        <input type="submit">
    </div>

</body>
</html>
```

