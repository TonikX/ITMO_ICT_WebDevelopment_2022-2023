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

host = "localhost"
port = 2468
message = "Hello, client! I'm happy to meet you too!"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
while True:
    received_message, address = server.recvfrom(4096)
    print("Client said: ", received_message.decode("utf-8"))
    server.sendto(message.encode("utf-8"), address)
    server.close()
    break
```

* `Клиентская часть, файл client.py`
``` python
import socket

host = "localhost"
port = 2468
message = "Hello, server! Nice to meet you!"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
client.sendto(message.encode("utf-8"), (host, port))
received_message, address = client.recvfrom(4096)
print("Server said: ", received_message.decode("utf-8"))
client.close()
```

## Задание №2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. В моём случае необходимо было реализовать расчёт площади трапеции.

Обязательно использовать библиотеку `socket`.

Реализовать с помощью протокола TCP.

* `Серверная часть, файл server.py`
``` python
import socket

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
connection, address = server.accept()

a = str()
b = str()
h = str()
area = str()

while not area:
    while not a:
        connection.sendto("Upper base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        a = float(data)
    while not b:
        connection.sendto("Lower base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        b = float(data)
    while not h:
        connection.sendto("The height of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        h = float(data)

    area = 0.5 * (a + b) * h
    connection.sendto(str.encode(f"The area of this trapezoid is {area}", encoding="utf-8"), address)

connection.close()
```

* `Клиентская часть, файл client.py`
``` python
import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
a = input("Enter the length of the upper base of the trapezoid: ")
print()
b = input("Enter the length of the lower base of the trapezoid: ")
print()
h = input("Enter the length of the height of the trapezoid: ")
print()
a = a.encode("utf-8")
b = b.encode("utf-8")
h = h.encode("utf-8")
while not a.isdigit():
    print("The length of the upper base of the trapezoid must be a number! Try again, please!")
    print()
    a = input("Enter the length of the upper base of the trapezoid: ")
    print()
    a = a.encode("utf-8")
while not b.isdigit():
    print("The length of the lower base of the trapezoid must be a number! Try again, please!")
    print()
    b = input("Enter the length of the lower base of the trapezoid: ")
    print()
    b = b.encode("utf-8")
while not h.isdigit():
    print("The length of the height of the trapezoid must be a number! Try again, please!")
    print()
    h = input("Enter the length of the height of the trapezoid: ")
    print()
    h = h.encode("utf-8")

while True:
    data = client.recv(4096)
    data = data.decode("utf-8")
    if data == "Upper base of the trapezoid":
        client.sendto(a, (host, port))
    if data == "Lower base of the trapezoid":
        client.sendto(b, (host, port))
    if data == "The height of the trapezoid":
        client.sendto(h, (host, port))
    if data.startswith("The area"):
        print(f"Server calculated the area of the trapezoid with next parameters:\n"
              f"    1) Length of the upper base of the trapezoid: {float(a)}\n"
              f"    2) Length of the lower base of the trapezoid: {float(b)}\n"
              f"    3) Length of the height of the trapezoid: {float(h)}\n")
        print(data)
        break

client.close()
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
    <title>Results of the second round of the group stage of the Champions League season 2022/2023</title>
</head>
<body>
  <h1> Group A </h1>
  <article>
    Liverpool 2:1 Ajax
    <br />
    Rangers 0:3 Napoli
  </article>
  <h1> Group B </h1>
  <article>
    Bayer 2:0 Atletico
    <br />
    Portu 0:4 Brugge
  </article>
  <h1> Group C </h1>
  <article>
    Victoria Plzen 0:2 Inter
    <br />
    Bayern Munich 2:0 Barcelona
  </article>
  <h1> Group D </h1>
  <article>
    Sporting 2:0 Tottenham
    <br />
    Marseille 0:1 Eintracht
  </article>
  <h1> Group E </h1>
  <article>
    Milan 3:1 Dinamo Zagreb
    <br />
    Chelsea 1:1 Red Bull Salzburg
  </article>
  <h1> Group F </h1>
  <article>
    Shakhtar Donetzk 1:1 Celtic
    <br />
    Real Madrid 2:0 Red Bull Leipzig
  </article>
  <h1> Group G </h1>
  <article>
    Manchester City 2:1 Borussia Dortmund
    <br />
    Copenhagen 0:0 Sevilla
  </article>
  <h1> Group H </h1>
  <article>
    Maccabi Haifa 1:3 PSG
    <br />
    Juventus 1:2 Benfica
  </article>
</body>
</html>
```

* `Серверная часть, файл server.py`
``` python
import socket

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
while True:
    connection, address = server.accept()
    page = open("index.html")
    info = page.read()
    page.close()
    data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + info
    connection.sendto(data.encode("utf-8"), address)
    print("Client receive the information")
    break

connection.close()
```

* `Клиентская часть, файл client.py`
``` python
import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()
```

## Задание №4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

Обязательно использовать библиотеку `socket`.

Обязательно использовать библиотеку `threading`.

Для реализации с помощью UDP, thearding использовать для получения
сообщений у клиента.

Для применения с TCP необходимо запускать клиентские подключения И прием
и отправку сообщений всем юзерам на сервере в потоках. Не забудьте сохранять юзеров,
чтобы потом отправлять им сообщения. 

Я реализовывал вариант с TCP.

* `Серверная часть, файл server.py`
``` python
import socket
import threading

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("The chat has been started!")

clients = []
users = []


def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)


def handle(client):
    while True:
        message = client.recv(8192)
        if message.decode("utf-8") == "leave":
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
        connection, address = server.accept()
        message = "What's your username?"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192)
        user = user.decode("utf-8")
        users.append(user)
        clients.append(connection)
        message = "You have entered the chat! Welcome!"
        connection.sendto(message.encode("utf-8"), address)
        message = "Type word 'leave' to leave this chat"
        connection.sendto(message.encode("utf-8"), address)
        message = "{} has entered this chat.".format(user)
        broadcast(message.encode("utf-8"), connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()
```

* `Клиентская часть, файлы client1.py, client2.py, client3.py (реализации одинаковы, несколько файлов было создано для удобства запуска)`
``` python
import socket
import threading


host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
user = input("What's your username? Enter it here, please: ")


def receiving_message():
    while True:
        message = client.recv(8192)
        message = message.decode("utf-8")
        if message == "What's your username?":
            client.sendto(user.encode("utf-8"), (host, port))
        else:
            print(message)


def sending_message():
    while True:
        text = input("")
        if text == "leave":
            client.sendto(text.encode("utf-8"), (host, port))
            print("You left this chat!")
            client.close()
            break
        else:
            message = "{}: {}".format(user, text)
            client.sendto(message.encode("utf-8"), (host, port))


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()
```

## Задание №5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки `socket`.

Сервер должен уметь принимать и записывать информацию о дисциплине и оценке по дисциплине, а также выдавать информацию обо всех оценках по дисциплине в виде html-страницы.

* `Файл response.py с классом Response`
``` python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```

* `Серверная часть, файл server.py`
``` python
import socket
from response import Response


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.points = {"Data science": ["100", "95", "76"],
                      "Theory of chances": ["100", "84"],
                      "Philosophy": ["92", "84", "73", "61", "100"]}

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
            raise Exception("Wrong number of points! Please, enter a number between 0 and 103.")
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
    port = 2468
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
```

