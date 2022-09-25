# Лабораторная работа №1

## Задача №1

* `server.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8071))
sock.listen(5)
client_socket, addr = sock.accept()
print(client_socket.recv(1024).decode("utf-8"))
client_socket.send(b"Hello, client")
sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8071))
sock.send(b"Hello, server")
print(sock.recv(1024).decode("utf-8"))
sock.close()
```

## Задача №2

* `server.py`

```python
import math
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8091))
sock.listen(10)
client_socket, addr = sock.accept()
client_socket.send(b"Hello, client\nPlease enter the coefficients a, b, c of your equation like ax^2+bx+c=0")
coefs = client_socket.recv(1024).decode("utf-8")
'''
https://younglinux.info/python/task/quadratic
'''
a = float(coefs[0])
b = float(coefs[2])
c = float(coefs[4])
discr = b ** 2 - 4 * a * c

if discr < 0:
    msg = "No real roots"
elif discr == 0:
    x = -b / (2 * a)
    msg = "x = %.2f" % x
else:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    msg = "x1 = %.2f \nx2 = %.2f" % (x1, x2)

client_socket.send(msg.encode("utf-8"))
sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8091))
print(sock.recv(1024).decode("utf-8"))
coefs = input("Enter a, b, c divided by space: ").encode("utf-8")
sock.send(coefs)
print(sock.recv(1024).decode("utf-8"))
sock.close()
```

## Задача №3

* `server.py`

```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 8901))
conn.listen(10)

while True:
    try:
        client_socket, addr = conn.accept()
        client_socket.recv(1024)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        f = open("index.html", "r")
        body = f.read()
        res = response_type + headers + body
        client_socket.send(res.encode("utf-8"))
        f.close()
        client_socket.close()
    except KeyboardInterrupt:
        conn.close()
        break
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main</title>
</head>
<body>
<h1>Hello, client</h1>
</body>
</html>
```

## Задача №4

* `server.py`

```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(('127.0.0.1', 8902))

clients = []
while True:
    try:
        data, client_address = conn.recvfrom(1024)
        if client_address not in clients:
            clients.append(client_address)
        for client in clients:
            if client != client_address:
                conn.sendto(data, client)
    except KeyboardInterrupt:
        conn.close()
        break

```

* `client.py`

```python
import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(('127.0.0.1', 8902))


def messages():
    while True:
        data = conn.recv(2048)
        print(data.decode("utf-8"))


def chat():
    name = input("Enter your name: ")
    print(f'{name}, say hello to the chat')
    conn.sendall(bytes(f"{name} joined", "utf-8"))
    while True:
        conn.sendto(bytes(f"{name}: {input()}", "utf-8"), ('127.0.0.1', 8902))


thread1, thread2 = threading.Thread(target=messages), threading.Thread(target=chat)
thread1.start(), thread2.start()
```

## Задача №5

* `server.py`

```python
import socket
import sys


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self._server_name = name

    # 1. Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                client, addr = serv_sock.accept()
                self.serve_client(client)

        finally:
            serv_sock.close()

    # 2. Обработка клиентского подключения
    def serve_client(self, client):
        try:
            method, url, version, params, headers = self.parse_request(client)
            self.handle_request(method, url, headers, client, params)
        except ConnectionResetError:
            client = None
        if client:
            client.close()

    # 3. функция для обработки заголовка http+запроса.Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола). URL необходимо разбить на адрес и параметры
    def parse_request(self, client):
        rfile = client.makefile('rb')
        method, url, version, params = None, None, None, None
        for line in rfile:
            words = line.decode('utf-8', errors='ignore').split()
            if len(words) != 3:
                raise Exception('Malformed request line')
            method, url, version = words
            # проверяем, есть ли параметры
            if "?" in url:
                url, params = url.split('?')
            break
        headers = self.parse_headers(rfile)
        return method, url, version, params, headers

    # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    @staticmethod
    def parse_headers(rfile):
        headers = []
        for line in rfile:
            if line in (b'\r\n', b'\n', b''):
                break
            headers.append(line)
        return headers

    # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор условий,
    # который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
    def handle_request(self, method, url, headers, client, params):
        if url == "/":
            if method == "GET":
                pass
            if method == "POST" and params is not None:
                data = params.split('&')
                discipline.append(data[0].split('=')[1])
                mark.append(data[1].split('=')[1])
        self.send_response(client)
        return

    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    @staticmethod
    def send_response(client):
        resp = "HTTP/1.1 200 OK\n\n"
        with open('index.html', 'r') as f:
            for line in f:
                if '<div id="on__server">\n' == line:
                    for i in range(len(discipline)):
                        resp += '<p id="on__server"> Discipline: ' + discipline[i] + ', Mark: ' + mark[i] + '</p>'
                resp += line
        client.send(resp.encode('UTF-8'))


if __name__ == '__main__':
    host = 'localhost'
    port = 9095
    name = 'example'
    serv = MyHTTPServer(host, port, name)
    discipline = []
    mark = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass

```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Journal</title>
    <style>
        body {
            margin: auto;
            text-align: center
        }

        .input__container {
            margin-bottom: 20px
        }
    </style>
</head>
<body>
<p>Hello, client</p>
<form name="input__form" id="form" method="post" accept-charset="UTF-8">
    <div class="input__container">
        <label for="Discipline"></label><input id="Discipline" class="discipline__input" name="Discipline" required
                                               type="text" placeholder="Discipline">
    </div>
    <div class="input__container">
        <label for="Mark"></label><input id="Mark" class="mark__input" name="Mark" required type="number"
                                         placeholder="Mark" value="value">
    </div>
    <div class="button__container"></div>
</form>
<div id="on__server">
</div>
<script>
    function submit() {
        let discipline = document.querySelector('.discipline__input');
        let mark = document.querySelector('.mark__input');
        fetch(`/?Discipline=${discipline.value}&Mark=${mark.value}`, {
            method: 'POST'
        })
    }

    let button = document.createElement('button');
    button.onclick = (submit)
    button.innerHTML = 'Submit'
    document.querySelector('.button__container').append(button);
</script>
</body>
</html>
```