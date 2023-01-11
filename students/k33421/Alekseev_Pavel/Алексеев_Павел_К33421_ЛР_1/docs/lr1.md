# Лабораторная работа №1

## Задача №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

* `server.py`


```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(100)
sock, addr = sock.accept()

client_to_server = sock.recv(2048)
print("Data from client: " + client_to_server.decode("utf-8"))

server_to_client = b"Hello, client!"
sock.send(server_to_client)

sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))


client_to_server = b"Hello, server!"
sock.send(client_to_server)

server_to_client = sock.recv(2048)
print("Data from server: " + server_to_client.decode("utf-8"))

sock.close()
```

## Задача №2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Теорема Пифагора

* `server.py`

```python
import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8001))
sock.listen(10)
sock, addr = sock.accept()

data_from_client = sock.recv(5096)
cat = data_from_client.decode("utf-8")

r = cat.split()
a = float(r[0])
b = float(r[1])
gep = round(math.sqrt(a**2 + b**2), 3)
ms_to_cl = str(gep)

sock.send(ms_to_cl.encode("utf-8"))

sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8001))

mess = input("Введите длину 2 катетов (через пробел) для рассчета гипотенузы : ").encode('utf-8')
sock.send(mess)

data = sock.recv(4096)
res = data.decode('utf-8')
print(f'Длина гипотенузы: ' + res)

sock.close()
```

## Задача №3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

* `server.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 7171))
sock.listen(10)
sock, addr = sock.accept()

file = open('index.html', 'r')

ht = 'HTTP/1.0 200 OK\n' + file.read()
sock.sendall(ht.encode("utf-8"))

file.close()
sock.close()


```
* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 7171))

data = sock.recv(4096)
print(data.decode('utf-8'))

sock.close()

```
* `index.html`
```html
<!DOCTYPE html>

<html lang="ru">
<head>

<meta charset="UTF-8">

<title> Test page </title>
</head>

<body>

Test page! DONE!
</body>

</html>
```

## Задача №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

* `server.py`

```python
import socket, threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen()

clients = []
users = []


def broadcast(sms, client):
    for each in clients:
        if each != client:
            each.send(sms)


def handle(client):
    while True:
        sms = client.recv(2000)
        broadcast(sms, client)


def receive():
    while True:
        client, addr = sock.accept()
        client.send('username'.encode())
        user = client.recv(2000).decode()
        clients.append(client)
        users.append(user)
        client.send('Пользователь в чате'.encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
```

* `client.py`


```python
import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1', 8080
sock.connect(server)

name = input('Выберите псевдоним: ')

def sms_write():
    while True:
        sms = name + ' написал: {}'.format(input(''))
        sock.send(sms.encode())

def sms_recive():
    while True:
        sms = sock.recv(2000).decode()
        if sms == 'username':
            sock.send(name.encode())
        else:
            print(sms)

recive_thr = threading.Thread(target=sms_recive)
write_thr = threading.Thread(target=sms_write)

recive_thr.start()
write_thr.start()
```

## Задача №5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:

Принять и записать информацию о дисциплине и оценке по дисциплине.

Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

* `server.py`

```python
import socket

class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.marks = []

    def serve_forever(self):

        serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serve_socket.bind((self.host, self.port))
        serve_socket.listen(10)
        print('good')
        while True:
            client_socket, address = serve_socket.accept()
            self.serve_client(client_socket)

    def serve_client(self, sock):

        data = sock.recv(4096).decode("utf-8")
        request = self.parse_request(data)
        response = self.handle_request(request)
        sock.send(response.encode())

    def parse_request(self, data):

        request_line = data.split('\r\n')[0]
        words = request_line.split()
        if len(words) == 3:
            try:
                par = data.split('\r\n')[-1]
                param = {}
                for p in par.split("&"):
                    param[p[:p.index('=')]] = p[p.index('=') + 1:]
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": param}
            except:
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": {}}
        else:
            raise Exception('Malformed request line')
        print(req)
        return req

    def parse_headers(self, data):
        lines = data.split('\r\n')[1:]
        headers = {}
        for line in lines:
            parts = line.split(': ')
            headers[parts[0]] = parts[1]
        return headers

    def handle_request(self, request):
        response = f"{request['version']} 200 OK\n\n"

        if request['method'] == 'GET' and request['url'] == "/":
            with open('insert.html') as page:
                response += page.read()
        elif request['method'] == 'GET' and request['url'] == "/view":
            body = '<!DOCTYPE html>' \
               '<html lang="ru">' \
               '<head>' \
               '<meta charset="UTF-8">' \
               '<title>Оценки</title>' \
               '</head>' \
               '<body>' \
               '<table align="center" width="20%" border="1">'
            for subject, mark in self.marks:
                body +=f"<tr><td>{subject}</td><td>{mark}</td></tr>"
            body += '</table></body></html>'
            response += body
        elif request['method'] == 'POST':
            self.marks.append((request['parametrs']['subject'], request['parametrs']['mark']))

        return response

if __name__ == '__main__':
    host = 'localhost'
    port = 5011
    name = 'aaaa.ru'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

* `insert.html`

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