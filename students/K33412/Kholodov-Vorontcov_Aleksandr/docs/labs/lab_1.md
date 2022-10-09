#Лабораторная работа №1 - Работа с сокетами 

##Цель 
* Овладеть практическими навыками и умениями реализации web-серверов и использования сокетов.
##Используемое ПО
* Python 3.10, библиотеки Python: sys, socket.
##Практическое задание:
###Задание №1:
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket

sock = socket.socket()
sock.bind(('localhost', 7777))
sock.listen(1)
clientSocket, addr = sock.accept()

print('connected:', addr)

while True:
    data = clientSocket.recv(1024)
    data = data.decode('utf-8')
    print(data)
    if not data:
        break
    clientSocket.send('Hello, client'.encode('utf-8'))

sock.close()
```

* `client.py`
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 7777))
sock.send('Hello, server'.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))
```

###Задание №2:
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера решение квадратного уравнения. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket
from math import sqrt


def quadratic_equation(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return f"{(-b + sqrt(b ** 2 - 4 * a * c)) / 2 * a}", f"{(-b - sqrt(b ** 2 - 4 * a * c)) / 2 * a}"
    else:
        return "No real roots"


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 7778))
    sock.listen()
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    a = ""
    b = ""
    c = ""
    result = ""

    while not result:
        while not a:
            conn.send('a'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                a = float(data)

        while not b:
            conn.send('b'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                b = float(data)

        while not c:
            conn.send('c'.encode('utf-8'))
            data = conn.recv(1024).decode('utf-8')
            if data.isdigit():
                c = float(data)

        result = quadratic_equation(a, b, c)
        conn.send(str.encode(f"Result is {result}"))

    conn.close()


if __name__ == "__main__":
    server()
```

* `client.py`
```python
import socket


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 7778))
    print("Quadratic equation solver")
    a = ""
    while not a.isdigit():
        a = input("Insert 'a': ")
    b = ""
    while not b.isdigit():
        b = input("Insert 'b': ")
    c = ""
    while not c.isdigit():
        c = input("Insert 'c': ")

    while True:
        data = sock.recv(1024).decode('utf-8')
        if data == 'a':
            sock.send(a.encode('utf-8'))
        if data == 'b':
            sock.send(b.encode('utf-8'))
        if data == 'c':
            sock.send(c.encode('utf-8'))
        if data.startswith("Result"):
            print(data)
            break


if __name__ == "__main__":
    client()
```

###Задание №3:
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket


class MyServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def serve_forever(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            while True:
                client, address = self.server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            self.server.close()

    def serve_client(self, client):
        html = self.handle_request()
        self.send_response(client, html)
        client.close()

    @staticmethod
    def handle_request():
        with open("index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, client, html):
        client.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode())


if __name__ == '__main__':
    MyServer('127.0.0.1', 7779, 'sample.com').serve_forever()
```

* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task 3</title>
</head>
<body>
  <h1>Hi, there!</h1>
  <article>
    This is a random text for task 3 of Lab 1 in Web-programming course 2022-2023. Actually got no idea if someone is ever going to read this but anyway have a good day!
  </article>
</body>
</html>
```

###Задание №4:
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов. Обязательно использовать библиотеку threading.

* `server.py`
```python
import socket
import threading


class MyChat:
    def __init__(self, ip, host):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((ip, host))
        self.sock.listen()
        self.clients = {}  # {client:alias}

    def broadcast(self, message, alias):
        for client in self.clients.keys():
            client.send(f"{alias}: {message}".encode())

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message, self.clients[client])
            except:
                client.close()
                self.broadcast(f'{self.clients[client]} has left the chat...'.encode('utf-8'))
                self.clients.pop(client)
                break

    def receive(self):
        print("Server is running")
        while True:
            client, address = self.sock.accept()
            print(f"{str(address)} connected!")
            client.send(b"What is your alias?")
            alias = client.recv(1024).decode()
            self.clients[client] = alias
            self.broadcast(f"{alias} has connected to the chat", "Server")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    MyChat("127.0.0.1", 7780).run()
```

* `client.py`
```python
import socket
import threading


class MyClient:
    def __init__(self, ip, port):
        self.alias = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()
                if message == "What's your alias?":
                    self.sock.send(self.alias.encode())
                else:
                    print(message)
            except:
                print("Error...")
                self.sock.close()
                break

    def send(self):
        while True:
            message = input()
            self.sock.send(message.encode())

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()


if __name__ == "__main__":
    MyClient("127.0.0.1", 7780).start()
```

###Задание №5:
Написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket, который может:
`принять и записать информацию о дисциплине и оценке по дисциплине`,
`отдать информацию обо всех оценках по дисциплине в виде html-страницы.`

* `server.py`
```python
import socket

grades = {}


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            serv_sock.bind((self.host, self.port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Fail', e)
        finally:
            serv_sock.close()

    def serve_client(self, client):
        try:
            req = self.parse_request(client)
            resp = self.handle_request(req)
            self.send_response(client, resp)
        except ConnectionResetError:
            client = None

        if client:
            client.close()

    def parse_request_line(self, rfile):
        line = rfile.readline()
        line = line.decode('utf-8')
        return line.split()

    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)

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
        body += '<form><label>Subject</label><input name="discipline" /><br><br><label>Grade</label><input name="grade"/><br><br><input type="submit"></form>'
        for subject in grades:
            body += f'<div><span>{subject}: {grades[subject]}</span></div>'
        body += '</div></body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in grades:
            grades[discipline] = []

        grades[discipline].append(grade)

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


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


if __name__ == '__main__':
    serv = MyHTTPServer('127.0.0.1', 7781)
    serv.serve_forever()
```