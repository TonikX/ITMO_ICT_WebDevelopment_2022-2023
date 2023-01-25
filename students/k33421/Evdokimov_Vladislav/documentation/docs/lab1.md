# Лабораторная работа №1. Евдокимов Владислав К33421



## Описание
		  Работа с сокетами

Цель: овладеть практическими навыками и умениями реализации web-серверов и
использования сокетов.



## Task 1:
```
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP
```
	client.py
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6666))

sock.send(bytes("Hello, server!!!", "utf-8"))
msg = sock.recv(1024)
print(msg.decode("utf-8"))
```
```
   server.py
```
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 6666))
sock.listen(1)

clientsocket, addr = sock.accept()
msg = clientsocket.recv(1024)
print(msg.decode("utf-8"))
clientsocket.send(bytes("Hello, client!!!!", "utf-8"))

clientsocket.close()
```

## Task 2:
```
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Вариант: Поиск площади параллелограмма.
```
```
client.py

```
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5675))

while True:
    try:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        sock.send(input().encode('utf-8'))
    except KeyboardInterrupt:
        sock.close()
        break

sock.close()


```
```
server.py
```
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 5675))
sock.listen(1)
conn, addr = sock.accept()

while True:
    conn.send("Enter figure's base and height lengths in form like x, y:".encode('utf-8'))
    try:
        data = conn.recv(1024)
        a, h = data.decode('utf-8').split(', ')
        s = (int(a) * int(h))
        print('Area is', s)
    except KeyboardInterrupt:
        conn.close()
        break
sock.close()
```
	
## Task 3:
```
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.
```
```
client.py
```

```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 6060))

while True:
    data = sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))

sock.close()
```

```
server.py
```

```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 6060))
sock.listen(1)

conn, addr = sock.accept()
conn.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open("index.html", "rb").read())

conn.close()
```
```
index.html
```

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Hey there fella</h1>
</body>
</html>
```

## Task 4:
```
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.
Обязательно использовать библиотеку.
Для реализации с помощью UDP, thearding использовать для получения
сообщений у клиента.
Для применения с TCP необходимо запускать клиентские подключения И прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения.
```
```
server4.py
```

```
import asyncio
import socket

connections = []

async def handle_client(client, address):
    request = None
    while request != 'покинуть':
        request = (await loop.sock_recv(client, 255)).decode('utf8')
        response = f'User{address}: ' + str(request)
        if request == 'покинуть':
            response = f'User {address} left the chat'
        for client_ in connections:
            if client_ == client:
                continue
            await loop.sock_sendall(client_, response.encode('utf8'))
    connections.remove(client)
    print(f'Client: {address} disconnected')
    client.close()


async def run_server():
    while True:
        client, address = await loop.sock_accept(server)
        if client not in connections:
            connections.append(client)
        print(f'Client {address} connected to the chat!')
        loop.create_task(handle_client(client, address))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 53330))
server.listen(8)
server.setblocking(False)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_server())
```

```
client4_1.py
```

```
import socket
from threading import Thread


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def get(self):
        while True:
            try:
                data = self._socket.recv(1024)
                print(data.decode('utf-8'))
            except OSError:
                exit()

    def send(self):
        while True:
            message = input()
            if message == 'покинуть':
                self._socket.send(bytes(f'{message}', 'utf-8'))
                self._socket.close()
                break
            self._socket.send(bytes(f'{message}', 'utf-8'))


if __name__ == '__main__':
    clint = Client(53330)
    th_1, th_2 = Thread(target=clint.send), Thread(target=clint.get)
    th_1.start(), th_2.start()
```

```
client4_2.py
```

```
import socket
from threading import Thread


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def get(self):
        while True:
            try:
                data = self._socket.recv(1024)
                print(data.decode('utf-8'))
            except OSError:
                exit()

    def send(self):
        while True:
            message = input()
            if message == 'покинуть':
                self._socket.send(bytes(f'{message}', 'utf-8'))
                self._socket.close()
                break
            self._socket.send(bytes(f'{message}', 'utf-8'))


if __name__ == '__main__':
    clint = Client(53330)
    th_1, th_2 = Thread(target=clint.send), Thread(target=clint.get)
    th_1.start(), th_2.start()
```

```
client4_3.py
```

```
import socket
from threading import Thread


class Client:
    def __init__(self, port):
        self._socket = socket.socket(family=socket.AF_INET,
                                     type=socket.SOCK_STREAM,
                                     proto=0)
        self._socket.connect(('127.0.0.1', port))

    def get(self):
        while True:
            try:
                data = self._socket.recv(1024)
                print(data.decode('utf-8'))
            except OSError:
                exit()

    def send(self):
        while True:
            message = input()
            if message == 'покинуть':
                self._socket.send(bytes(f'{message}', 'utf-8'))
                self._socket.close()
                break
            self._socket.send(bytes(f'{message}', 'utf-8'))


if __name__ == '__main__':
    clint = Client(53330)
    th_1, th_2 = Thread(target=clint.send), Thread(target=clint.get)
    th_1.start(), th_2.start()
```

## Task 5:
```
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Задание: сделать сервер, который может:
● Принять и записать информацию о дисциплине и оценке по дисциплине.
● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.
```
```
server5.py
```

```
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
        resp = self.handle_request(method, body)
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

    def handle_request(self, method, body):
        if method == "GET":
            resp = "HTTP/1.1 200 OK\n\n"
            with open('index.html') as f:
                resp += f.read()
            return resp

        if method == "POST":
            newbody = body.split('&')
            for content in newbody:
                if content.split('=')[0] == 'subject':
                    subjects.append(content.split('=')[1])
                if content.split('=')[0] == 'mark':
                    marks.append(content.split('=')[1])

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
    port = 6767
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

```
```
index.html
```

```
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