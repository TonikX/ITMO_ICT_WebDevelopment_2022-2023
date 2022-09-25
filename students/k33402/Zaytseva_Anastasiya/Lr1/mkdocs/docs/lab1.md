# Лабораторная работа №1

## Задача №1

* `server.py`
```python
import socket

HELLO_MESSAGE = 'Hello, client'
LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание UDP сокета
sock.bind(('', LOCAL_PORT))  # привязка сокета к локальному порту

while True:  # в бесконечном цикле
    data, address = sock.recvfrom(BUFFER_SIZE)   # получаем данные и адрес от клиента
    print(data.decode("utf-8"))  # выводим полученные данные
    sock.sendto(HELLO_MESSAGE.encode("utf-8"), address)  # отправляем ответное сообщение по адресу
```

* `client.py`
```python
import socket

HELLO_MESSAGE = 'Hello, server'
LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание UDP сокета
sock.sendto(HELLO_MESSAGE.encode("utf-8"), ("localhost", LOCAL_PORT))  # отправляем сообщение по адресу сервера
data = sock.recv(BUFFER_SIZE)  # получаем ответное сообщение
print(data.decode("utf-8"))  # выводим ответное сообщение
```

## Задача №2
* `server.py`
```python
import socket
from math import sqrt

LOCAL_PORT = 25030
MAX_CLIENTS = 1
BUFFER_SIZE = 1024

sock = socket.socket()  # создание TCP сокета
sock.bind(('', LOCAL_PORT))  # привязка сокета к локальному порту
sock.listen(MAX_CLIENTS)  # установка ограничения на максимальное число подключенных клиентов
conn, addr = sock.accept()  # принимаем подключение 1 клиента
print('Соединение установлено.')

step = 1
with_hypo_input = False
side_a = 0
side_b = 0


def solve_pyth(a, b, with_hypo):  # функция для нахождения стороны треугольника по теореме Пифагора
    high = a if a > b else b
    low = a if a < b else b
    return sqrt(high * high + low * low * (-1 if with_hypo else 1))


while True:  # в бесконечном цикле
    data = conn.recv(1024)  # получаем сообщение клиента
    if not data:
        break
    message = data.decode('utf-8')

    if message == 'завершить':  # завершаем работу по команде клиента
        break
    if step == 1:  # в зависимости от текущего шага алгоритма, запрашиваем у клиента данные
        conn.send('Вы собираетесь вводить гипотенузу? (да/нет)'.encode('utf-8'))
        print('Отправлен вопрос про гипотенузу.')
        step += 1
    elif step == 2:
        if message.lower() == 'да':
            with_hypo_input = True
        print('Получен ответ: ' + message)
        conn.send('Пожалуйста, введите первую сторону.'.encode('utf-8'))
        print('Отправлен запрос первой стороны.')
        step += 1
    elif step == 3:
        side_a = float(message)
        print('Получен ответ: ' + message)
        conn.send('Пожалуйста, введите вторую сторону.'.encode('utf-8'))
        print('Отправлен запрос второй стороны.')
        step += 1
    elif step == 4:
        print('Получен ответ: ' + message)
        side_b = float(message)
        side_c = solve_pyth(side_a, side_b, with_hypo_input)
        print('Отправлено решение: ' + str(side_c))
        conn.send(('Третья сторона: ' + str(side_c)).encode('utf-8'))
        step = 1

conn.close()
```

* `client.py`
```python
import socket

LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket()  # создаем TCP сокет
sock.connect(('localhost', LOCAL_PORT))  # подключаемся к локальному серверу

while True:  # в бесконечном цикле
    message = input()  # считываем ввод пользователя
    if message.lower() == 'exit':  # если введено "exit", завершаем выполнение
        break
    sock.send(message.encode('utf-8'))  # отправляем введенное сообщение
    data = sock.recv(BUFFER_SIZE)  # получаем ответ от сервера
    print(data.decode('utf-8'))  # выводим ответ

sock.close()
```

## Задача №3
* `server.py`
```python
import socket
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime

LOCAL_PORT = 25030
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

SERVER_NAME = 'chiclasserver/1.0.0'

sock = socket.socket()
sock.bind(('', LOCAL_PORT))
sock.listen(MAX_CLIENTS)

with open('index.html', 'r') as file:  # чтение файла
    file_data = file.read()

now = datetime.now()  # вычисляем время в нужном формате для подстановки в поле даты
stamp = mktime(now.timetuple())
date = format_date_time(stamp)

dt = datetime.strptime('24/09/22 15:08', '%d/%m/%y %H:%M')  # вычисляем время в нужном формате для подстановки в поле
# последней модификации файла
stamp = mktime(dt.timetuple())
last_modified = format_date_time(stamp)

content_length = len(file_data.encode('utf-8'))  # вычисляем размер файла

data = f'''HTTP/1.1 200 OK
Server: {SERVER_NAME}
Date: {date}
Content-Type: text/html
Content-Length: {content_length}
Last-Modified: {last_modified}
Connection: keep-alive
Access-Control-Allow-Origin: *
Accept-Ranges: bytes

'''

data += file_data

while True:
    conn, addr = sock.accept()
    conn.send(data.encode('utf-8'))
    print('index.html был отправлен')
    conn.close()
```

* `client.py`
```python
import socket

LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket()
sock.connect(('localhost', LOCAL_PORT))

data = sock.recv(BUFFER_SIZE)
print(data.decode('utf-8'))

sock.close()
```

* `index.html`
```html
<!DOCTYPE html>
<html>
<head>
    <title>Web programming lab 1</title>
</head>
<body>
    <h1>Hello world</h1>
</body>
</html>
```

## Задача №4
* `server.py`
```python
import socket
from _thread import *

LOCAL_PORT = 25030
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

sock = socket.socket()
sock.bind(('', LOCAL_PORT))
sock.listen(MAX_CLIENTS)

list_of_users = []  # список пользователей


def client_thread(user):  # функция получения и обработки сообщений пользователя
    connection = user[0]
    connection.send('Добро пожаловать в чат!'.encode('utf-8'))

    while True:
        try:
            name = user[1]
            data = connection.recv(1024)
            if data:
                message = data.decode('utf-8')
                if name == '':  # если имя не присвоено, присваимваем
                    user[1] = message
                    print('Новый пользователь: ' + message)
                    broadcast(message + ', добро пожаловать в чат!', connection)
                else:
                    message_to_send = name + ': ' + message
                    broadcast(message_to_send, connection)

            else:
                if user in list_of_users:
                    list_of_users.remove(user)
        except:
            continue


def broadcast(message, connection):  # функция рассылки сообщения всем пользователям чата, кроме выбранного
    for user in list_of_users:
        user_conn = user[0]
        if user_conn != connection:
            try:
                user_conn.send(message.encode('utf-8'))
            except:
                if user in list_of_users:
                    list_of_users.remove(user)


while True:  # в бесконечном цикле принимаем новые подключения и создаем на каждое отдельный поток
    conn, addr = sock.accept()
    list_of_users.append([conn, ''])
    print(addr[0] + " connected")
    start_new_thread(client_thread, (list_of_users[len(list_of_users) - 1],))

sock.close()
```

* `client.py`
```python
import socket
import _thread

LOCAL_PORT = 25030
BUFFER_SIZE = 1024


def handle_messages(connection):
    while True:
        msg = connection.recv(1024)
        if not msg:
            connection.close()
            break
        print(msg.decode('utf-8'))


sock = socket.socket()
print('Представьтесь, пожалуйста:')
name = input()  # считываем имя пользователя

sock.connect(('localhost', LOCAL_PORT))
print('Соединение установлено.')
_thread.start_new_thread(handle_messages, (sock,))  # в отдельном потоке запускам получение сообщений с сервера в
# бесконечном цикле

sock.send(name.encode('utf-8'))

while True:

    message = input()  # считываем сообщения для отправки в чат в бесконечном цикле
    if message == 'exit':  # завершаем выполнение при получении команды "exit"
        break
    sock.send(message.encode('utf-8'))

sock.close()
```

## Задача №5

* `server.py`
```python
import json
import socket
import sys
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._disciplines = {}

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except Exception as e:
            print(e)
            self.send_error(conn, e)

        if conn:
            conn.close()

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise HTTPError(400, 'Bad request',
                            'Host header is missing')
        if host not in (self._server_name,
                        f'{self._server_name}:{self._port}'):
            raise HTTPError(404, 'Not found')
        return Request(method, target, ver, headers, rfile)

    def parse_request_line(self, rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request',
                            'Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request',
                            'Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise HTTPError(494, 'Request header too large')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        return Parser().parsestr(sheaders)

    def handle_request(self, req):
        if req.path == '/disciplines' and req.method == 'POST':
            return self.handle_post_disciplines(req)

        if req.path == '/disciplines' and req.method == 'GET':
            return self.handle_get_disciplines(req)

        raise Exception('Not found')

    def send_response(self, conn, resp):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()

    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
        resp = Response(status, reason,
                        [('Content-Length', len(body))],
                        body)
        self.send_response(conn, resp)

    def handle_post_disciplines(self, req):
        discipline_id = len(self._disciplines) + 1
        self._disciplines[discipline_id] = {'id': discipline_id,
                                            'name': req.query['name'][0],
                                            'grade': req.query['grade'][0]}
        return Response(204, 'Created')

    def handle_get_disciplines(self, req):
        accept = req.headers.get('Accept')
        if 'text/html' in accept:
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<div>Дисциплины ({len(self._disciplines)})</div>'
            body += '<ul>'
            for u in self._disciplines.values():
                body += f'<li>#{u["id"]} {u["name"]}, {u["grade"]}</li>'
            body += '</ul>'
            body += '</body></html>'

        elif 'application/json' in accept:
            contentType = 'application/json; charset=utf-8'
            body = json.dumps(self._disciplines)

        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', contentType),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)


class Request:
    def body(self):
        size = self.headers.get('Content-Length')
        if not size:
            return None
        return self.rfile.read(size)

    def __init__(self, method, target, version, headers, rfile):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile

    @property
    def path(self):
        return self.url.path

    @property
    @lru_cache(None)
    def query(self):
        return parse_qs(self.url.query)

    @property
    @lru_cache(None)
    def url(self):
        return urlparse(self.target)


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body

class HTTPError(Exception):
  def __init__(self, status, reason, body=None):
    super()
    self.status = status
    self.reason = reason
    self.body = body

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3]

    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```