# Лабораторная работа №1

## Задача №1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

* `server.py`

```python
import socket

# UDP server
server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_sock.bind(('localhost', 9090))

while True:
    data, address = server_sock.recvfrom(1024)
    if data == b'Hello, server':
        print(data)
        server_sock.sendto(b'Hello, client', address)
    else:
        server_sock.close()
        break
```

* `client.py`

```python
import socket

# UDP client
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.connect(('localhost', 9090))
client_sock.sendto(b'Hello, server', ('localhost', 9090))
data, server = client_sock.recvfrom(1024)
client_sock.close()

print(data)
```

## Задача №2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. 

Теорема Пифагора

* `server.py`

```python
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 8081))
server_sock.listen(5)

while True:
    client_sock, client_addr = server_sock.accept()
    data = client_sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    client_sock.sendall('Enter the sides (for ex. 5,9)'.encode("utf-8"))

    data = client_sock.recv(1024)
    sides = data.decode("utf-8")

    try:
        a, b = map(int, sides.split(','))
        c = (a ** 2 + b ** 2) ** 0.5
        ans = str(round(c, 3))
        client_sock.sendall(ans.encode("utf-8"))
    except Exception:
        client_sock.sendall('Error. Try again'.encode("utf-8"))

    client_sock.close()
```

* `client.py`

```python
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 8081))
client_sock.sendall('Pyfagorean theorem'.encode("utf-8"))

data = client_sock.recv(1024)
print(data.decode("utf-8"))

sides = input()
client_sock.sendall(sides.encode("utf-8"))

data = client_sock.recv(1024)

client_sock.close()

print(data.decode("utf-8"))
```

## Задача №3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

* `server.py`

```python
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 8080))
server_sock.listen(5)

while True:
    client_sock, client_addr = server_sock.accept()
    data = client_sock.recv(1024)
    if not data:
        break
    status_line = "HTTP/1.0 200 OK\n"
    resp_headers = "Content-Type: text/html\n\n"
    body = open('index.html', 'r').read()
    response = status_line + resp_headers + body
    client_sock.sendall(response.encode("utf-8"))
    open('index.html', 'r').close()
    client_sock.close()
```

* `client.py`

```python
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 8080))
client_sock.sendall('Hi!'.encode("utf-8"))

data = client_sock.recv(1024)
print(data.decode("utf-8"))

client_sock.close()
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Message</title>
</head>
<body>
Hello from server!
</body>
</html>
```

## Задача №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.


* `server.py`

```python
import socket
import threading

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 9090))
server_sock.listen(5)

clients = dict()


# send message to everyone
def broadcast(message):
    for client in clients:
        client.sendall(message)


# handling a client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode("utf-8") == "{}:bye".format(clients[client]):
                broadcast('{} has left'.format(clients.pop(client)).encode("utf-8"))
                client.close()
                break
            broadcast(message)
        except:
            broadcast('{} has left'.format(clients.pop(client)).encode("utf-8"))
            client.close()
            break


def chat():
    while True:
        client_sock, client_addr = server_sock.accept()
        client_sock.sendall('Nick:'.encode("utf-8"))
        nick = client_sock.recv(1024).decode("utf-8")
        clients[client_sock] = nick
        broadcast('{} joined!'.format(nick).encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client_sock,))
        thread.start()

        
chat()
```

* `client.py`

```python
import socket
import threading

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 9090))

nick = input("Your nick: ")


def get_message():
    while True:
        try:
            message = client_sock.recv(1024)
            if len(message) == 0:
                client_sock.close()
                break

            if message.decode("utf-8") == 'Nick:':
                client_sock.sendall(nick.encode("utf-8"))
            else:
                print(message.decode("utf-8"))
        except:
            client_sock.close()
            break


def send_message():
    while True:
        try:
            text = input("")
            message = '{}:{}'.format(nick, text)
            client_sock.sendall(message.encode("utf-8"))
            if text == "bye":
                break
        except:
            client_sock.close()
            break


get_thread, send_thread = threading.Thread(target=get_message), threading.Thread(target=send_message)
get_thread.start()
send_thread.start()

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

MAX_LINE = 64 * 1024


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port):
        self._host = host
        self._port = port

    # Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((self._host, self._port))
        server_sock.listen(5)

        while True:
            client_sock, client_addr = server_sock.accept()
            try:
                self.serve_client(client_sock)
            except:
                server_sock.close()
                break

    # Обработка клиентского подключения
    def serve_client(self, client_sock):
        try:
            req_str = client_sock.recv(65536).decode("utf-8")
            method, url, params, headers, body = self.parse_request(req_str)
            resp = self.handle_request(method, url, params, headers, body)
            if resp is not None:
                self.send_response(client_sock, resp)
        except ConnectionResetError:
            client_sock = None

        if client_sock:
            client_sock.close()

    @staticmethod
    def parse_request(req_str):
        req_str.replace('\r', '')
        req_lines = req_str.split('\n')

        headers, method, url, version, body, params = dict(), "", "", "", "", ""
        body_start_idx = -1
        for i in range(0, len(req_lines)):
            line = req_lines[i]
            if i == 0:  # Если первая строка, то парсить как строку запроса
                words = line.split()  # разделяем по символам
                if len(words) != 3:  # ожидаем ровно 3 части
                    raise Exception('Malformed request line')

                method, url, version = words
                if '?' in url:
                    url, params = url.split('?')
                    params_strings = params.split("&")
                    params = dict()
                    for param_string in params_strings:
                        params[param_string.split("=")[0]] = param_string.split("=")[1]

                if version != 'HTTP/1.1':
                    raise Exception('Unexpected HTTP version')

                continue
            # Если строки заголовков или тела
            if not ":" in line:  # дальше тело
                body_start_idx = i + 1
                break

            # Еще заголовки
            headers[line.split(':')[0]] = line.split(':')[1]

        if body_start_idx != -1 and body_start_idx < len(req_lines):
            body = req_lines[body_start_idx:]

        return method, url, params, headers, body

    # Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор
    # условий, который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен
    # записывать данные на основе переданных параметров.
    @staticmethod
    def handle_request(method, url, params, headers, body):
        if not url == "/":
            return ""

        if method == "GET":
            if params == "":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as f:
                    resp += f.read()
                f.close()
                return resp

            if 'subject' in params and params['subject'] in subjects:
                subject = params['subject']
                resp = "HTTP/1.1 200 OK\n\n"
                resp += f"<html><head><title>Journal for {subject}</title></head><body>"
                resp += f"<p>{subject}: "
                for grade in subjects[subject]:
                    resp += f"{grade}, "
                resp = resp[:-2]
                resp += "</p>"
                resp += "</body></html>"
                return resp

            raise "invalid get request"

        if method == "POST":
            body_kvps = body[0].split('&')
            body_params = dict()
            for kvp in body_kvps:
                body_params[kvp.split('=')[0]] = kvp.split('=')[1]

            if 'subject' in body_params and 'grade' in body_params and len(body_params) == 2:
                subject = body_params['subject'].strip()
                grade = body_params['grade'].strip()
                if grade != '' and subject != '':
                    if subject not in subjects:
                        subjects[subject] = []

                    subjects[subject].append(grade)

            resp = "HTTP/1.1 200 OK\n\n"
            resp += "<html><head><title>Journal</title></head><body>"
            for subject in subjects:
                resp += f"<p>{subject}: "
                for grade in subjects[subject]:
                    resp += f"{grade}, "
                resp = resp[:-2]
                resp += "</p>"
            resp += "</body></html>"
            return resp

    # Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    @staticmethod
    def send_response(client_sock, resp):
        client_sock.sendall(resp.encode("utf-8"))


if __name__ == '__main__':
    host = 'localhost'
    port = 9091
    serv = MyHTTPServer(host, port)
    subjects = dict()
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
</head>
<body>
<form action="/" method="post">
        <label for="name">Subject:</label>
        <input type="text" id="name" name="subject"/>
        <label for="grade">Grade:</label>
        <input type="number" id="grade" name="grade"/>
        <input type="submit">
</form>
</body>
</html>
```
