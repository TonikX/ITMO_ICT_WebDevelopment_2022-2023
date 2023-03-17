# Лабораторная работа №1

## Задание №1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

Обязательно использовать библиотеку `socket`.

Реализовать с помощью протокола UDP.

* `Серверная часть, файл server.py`
``` python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))
data = sock.recvfrom(1024)
print(data[0].decode("utf-8"))
sock.sendto(b"hello, client! \n", data[1])
sock.close()

```

* `Клиентская часть, файл client.py`
``` python
import socket

addressPort = ('127.0.0.1', 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(addressPort)
sock.sendto(b"hello, world! \n", addressPort)

data = sock.recvfrom(1024)
sock.close()

print(data[0].decode("utf-8"))
```

## Задание №2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. В моём случае необходимо было реализовать расчёт длины гипотенузы.

Обязательно использовать библиотеку `socket`.

Реализовать с помощью протокола TCP.

* `Серверная часть, файл server.py`
``` python
import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(5)

while True:
    try:
        conn, addr = sock.accept()
        a, b = [int(i) for i in conn.recv(1024).decode('utf-8').split('\n')]
        c = math.sqrt(a*a+b*b)
        conn.send(str.encode(str(c)))
    finally:
        sock.close()
        break

```

* `Клиентская часть, файл client.py`
``` python
import socket

addressPort = ('127.0.0.1', 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addressPort)
a = int(input("Enter value a: "))
b = int(input("Enter value b: "))
sock.send(str.encode("\n".join([str(a), str(b)])))

data = sock.recv(1024)
print("Value c is: " + data.decode("utf-8"))
sock.close()
```

## Задание №3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

Обязательно использовать библиотеку `socket`.


* `Файл index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My html page</title>
</head>
<body>

    <p>
         Hello world or something..
    </p>

</body>
</html>
```

* `Серверная часть, файл server.py`
``` python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9090))
sock.listen(10)

while True:
    conn, addr = sock.accept()
    with open("index.html", "r") as f:
        index = f.read()
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'
    response = response_type + headers + index
    conn.send(response.encode("utf-8"))
    sock.close()

```

* `Клиентская часть, файл client.py`
``` python
import socket

addressPort = ('127.0.0.1', 9090)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addressPort)
data = sock.recv(1024)
print(data.decode("utf-8"))
sock.close()
```

## Задание №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

Обязательно использовать библиотеку `socket`.

Обязательно использовать библиотеку `threading`.

Для реализации с помощью UDP, threading использовать для получения
сообщений у клиента.

Для применения с TCP необходимо запускать клиентские подключения И прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения. 

Мною был реализован TCP вариант.

* `Серверная часть, файл server.py`
``` python
import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7070))
sock.listen(10)

clients = []
users = []


def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)


def handle(client):
    while True:
        message = client.recv(8192)
        if message.decode("utf-8") == "quit":
            i = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[i]
            users.remove(user)
            message = "{} left the chat.".format(user).encode("utf-8")
            broadcast(message, client)
            break
        broadcast(message, client)


def receive():
    while True:
        connection, address = sock.accept()
        message = "What's your username?"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192)
        user = user.decode("utf-8")
        users.append(user)
        clients.append(connection)
        message = "You have entered the chat! Welcome!"
        connection.sendto(message.encode("utf-8"), address)
        message = "Type word 'quit' to leave this chat"
        connection.sendto(message.encode("utf-8"), address)
        message = user + " has entered this chat."
        broadcast(message.encode("utf-8"), connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()

```

* `Клиентская часть, файлы client1.py, client2.py, client3.py `
``` python
import socket
import threading


addressPort = ('127.0.0.1', 7070)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addressPort)
user = input("Enter username: ")


def receiving_message():
    while True:
        try:
            message = sock.recv(1024)
            message = message.decode("utf-8")
            if message == "What's your username?":
                sock.sendto(user.encode("utf-8"), addressPort)
            else:
                print(message)
        finally:
            sock.close()


def sending_message():
    while True:
        text = input("")
        if text == "quit":
            sock.sendto(text.encode("utf-8"), addressPort)
            print("You left this chat!")
            sock.close()
            break
        else:
            message = user + ': ' + text
            sock.sendto(message.encode("utf-8"), addressPort)


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()

```

## Задание №5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки `socket`.

Сервер должен уметь принимать и записывать информацию о дисциплине и оценке по дисциплине, а также выдавать информацию обо всех оценках по дисциплине в виде html-страницы.

* `Серверная часть, файл server.py`
``` python
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
        self.points = {"Web-programming": ["99", "100", "98"],
                      "Storytelling": ["60", "62", "74"]}

    def serve_forever(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (self.host, self.port)
        try:
            server.bind(address)
            server.listen()
            while True:
                connection, address = server.accept()
                self.serve_client(connection)
        except KeyboardInterrupt:
            server.close()

    def serve_client(self, connection):
        try:
            data = connection.recv(4096)
            data = data.decode("utf-8")
            request = self.parse_request(data)
            result = self.handle_request(request)
            self.send_response(connection, result)
        except Exception as exception_text:
            print("Client connection failed: ", exception_text)
        connection.close()

    def parse_request(self, data):
        request = data.rstrip('\r\n')
        text = request[:data.index("\n")].split()
        if len(text) != 3:
            raise Exception('Malformed request line')

        method, target, version = text
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        request = {'data': {}, 'method': method}
        if '?' in target:
            request['method'] = 'POST'
            data = target.split('?')[1].split('&')
            for value in data:
                index, info = value.split('=')
                request['data'][index] = info

        return request

    def handle_request(self, request):
        if request['method'] == 'POST':
            return self.handle_post(request)
        else:
            return self.handle_get()

    def handle_get(self):
        type = "text/html; charset=utf-8"
        first_settings = "<html><head><style></style></head><body>"
        course = "<form><label>Name of discipline: </label><input name='course' /><br><br>"
        points = "<label>Number of points: </label><input name='points' /><br><br>"
        button = "<input type='submit'></form>"
        body = first_settings + course + points + button
        for course_name in self.points:
            body += f"<div><span>{course_name}: {self.points[course_name]}</span></div>"
        second_settings = "</body></html>"
        body += second_settings
        body = body.encode("utf-8")
        headers = [("Content-Type", type),
                   ("Content-Length", len(body))]
        return Response(200, "OK", headers, body)

    def handle_post(self, request):
        course = request["data"]["course"]
        points = request["data"]["points"]
        if course not in self.points:
            self.points[course] = []
        if int(points) < 0 or int(points) > 103:
            raise Exception("Wrong number of points! Please enter a number between 0 and 103.")
        self.points[course].append(points)
        return self.handle_get()

    def send_response(self, connection, response):
        file = connection.makefile('wb')
        status_line = f"HTTP/1.1 {response.status} {response.reason}\r\n"
        status_line = status_line.encode("utf-8")
        file.write(status_line)
        if response.headers:
            for (index, info) in response.headers:
                header_line = f"{index}: {info}\r\n"
                file.write(header_line.encode("utf-8"))
        file.write(b"\r\n")
        if response.body:
            file.write(response.body)
        file.flush()
        file.close()

    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == '__main__':
    host = 'localhost'
    port = 9095
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

```