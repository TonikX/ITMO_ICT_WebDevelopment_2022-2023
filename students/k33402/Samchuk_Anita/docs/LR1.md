# Лабораторная №1

## Задание №1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
### server_1.py
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9090))

while True:
    conn, addr = sock.recvfrom(1024)
    print('client addr: ', addr)

    sock.sendto(b'Hello, client', addr)

sock.close
```

### client_1.py
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('', 9090))
sock.send(b'Hello, server')

data = sock.recvfrom(1024)
sock.close

print(data[0].decode('utf-8'))
```
## Задание №2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту.
<b>Вариант: Теорема Пифагора
### server_2.py
```
import socket
from math import sqrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    udata = data.decode('utf-8').split(',')
    for i in range(len(udata)):
        udata[i] = int(udata[i])

    if udata[0] == 1:
        c = sqrt(udata[1]**2 + udata[2]**2)
    else:
        c = sqrt(max(udata[1], udata[2])**2 - min(udata[1], udata[2])**2)
        if c == 0:
            c = 'Вы ввели неверные данные'
    conn.send(str(c).encode('utf-8'))

conn.close
```

### client_2.py
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8080))

print('Что вам надо посчитать?\n1)Гипотенуза\n2)Катет')
answer = input()
print('Введите известные стороны')
a, b = map(int, input().split())
sock.send(f'{answer},{a},{b}'.encode('utf-8'))

data = sock.recv(1024)
sock.close
```
## Задание №3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.
### server_3.py
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 7070))
sock.listen(10)
conn, addr = sock.accept()

while True:
    html_page = open('index.html')
    html_content = html_page.read()
    html_page.close()

    html_response = 'HTTP/1.0 200 OK\n\n' + html_content

```

### index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>The room</title>
</head>
<body>
    <img src="https://c.tenor.com/d4NXy1SxPc0AAAAd/i-did-not-hit-her-its-not-true.gif" alt="The room">
</body>
</html>
```
## Задание №4
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.
### server_4.py
```
import socket
from threading import Thread

server_host = "0.0.0.0"
server_port = 6060
separator_token = "<SEP>"

client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((server_host, server_port))
s.listen(5)
print(f"[*] Listening as {server_host}:{server_port}")


def listen_for_client(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ": ")
        for client_socket in client_sockets:
            if client_socket != cs:
                client_socket.send(msg.encode())


while True:
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    client_sockets.add(client_socket)
    t = Thread(target=listen_for_client, args=(client_socket,), daemon=True)
    t.start()

for cs in client_sockets:
    cs.close()
s.close()

```

### client_4.py
```
import socket
from threading import Thread

server_host = "127.0.0.1"
server_port = 6060
separator_token = "<SEP>"

sock = socket.socket()
print(f"[*] Connecting to {server_host}:{server_port}...")
sock.connect((server_host, server_port))
print("[+] Connected.")
name = input("Enter your name: ")


def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print(message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    to_send = f"{name}{separator_token}{to_send}"
    sock.send(to_send.encode())

sock.close()
```
## Задание №5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
### server_5.py
```
import socket


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.marks = {}

    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self.host, self.port))
            serv_sock.listen()
            while True:
                client, address = serv_sock.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            serv_sock.close()

    def serve_client(self, client):
        try:
            data = client.recv(1024).decode('UTF-8')
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        except Exception as e:
            print(e)
        client.close()

    def parse_request(self, data):
        req = data.rstrip('\r\n')
        words = req[:data.index("\n")].split()
        if len(words) != 3:
            raise Exception('Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        request = {'data': {}, 'method': method}
        if '?' in target:
            request['method'] = 'POST'
            values = target.split('?')[1].split('&')
            for value in values:
                a, b = value.split('=')
                request['data'][a] = b

        return request

    def handle_request(self, req):
        if req['method'] == 'POST':
            return self.handle_post(req)
        else:
            return self.handle_get()

    def handle_get(self):
        content_type = 'text/html; charset=utf-8'
        body = '<html><head><style></style></head><body>'
        body += '<form method="GET"><label>Дисциплина</label>' \
                '<input name="discipline" />' \
                '<br><label>Оценка</label>' \
                '<input name="grade"/>' \
                '<input type="submit"></form>'
        for subject in self.marks:
            body += f'<div><span>{subject}: {self.marks[subject]}</span></div>'
        body += '</div></body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in self.marks:
            self.marks[discipline] = []

        self.marks[discipline].append(grade)

        return self.handle_get()

    def send_response(self, conn, resp):
        rfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        rfile.write(status_line.encode('utf-8'))

        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                rfile.write(header_line.encode('utf-8'))

        rfile.write(b'\r\n')

        if resp.body:
            rfile.write(resp.body)

        rfile.flush()
        rfile.close()


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000
    serv = MyHTTPServer(host, port)
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass
```
