# Laboratory 1

## Task 1
Клиент-серверное взаимодействие с помощью библиотеки `socket` и протокола `UDP`.
Клиент посылает данные серверу, а сервер — клиенту. Оба печатают полученные данные.

* `client.py`. 
``` python
import socket


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    serverAddressPort = ("localhost", 9091)

    sock.sendto(str.encode("Hello, server!"), serverAddressPort)

    data, address = sock.recvfrom(1024)
    print(data.decode())

if __name__ == "__main__":
    main()
```

* `server.py`
``` python
import socket, sys


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    sock.bind(("localhost", 9091))

    while True:
        data, address = sock.recvfrom(1024)
        print(data.decode())
        sock.sendto(str.encode("Hello, client!"), address)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
```

## Task 2
Клиент-серверное взаимодействие с помощью библиотеки `socket` и протокола `TCP`.
Клиент запрашивает у сервера площадь параллелограмма по введенным данным с клавиатуры.
Когда сервер получает данные, то он выполняет функцию `calc_parallelogram_area`, которая соответственно принимает два аргумента, и результат отсылает клиенту.

* `client.py`
``` python
import socket


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(("localhost", 9092))

    s, h = input(
        "Enter the side and height of the par-gram separated by a space: "
    ).split()
    sock.sendall(str.encode("\n".join([str(s), str(h)])))

    data = sock.recv(1024)
    sock.close()

    print(data.decode())


if __name__ == "__main__":
    main()
```

* `server.py`
``` python
import socket, sys


def calc_parallelogram_area(side, height):
    return side * height


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(("localhost", 9092))
    sock.listen(1)

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        s, h = [int(i) for i in data.decode().split("\n")]
        conn.send(str.encode(str(calc_parallelogram_area(s, h))))
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
```

## Task 3
Клиент-серверное взаимодействие с помощью библиотеки `socket` и протокола `TCP`.
Клиент подключается к серверу и получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла `index.html`.

* `server.py`
``` python
import socket, sys


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(("localhost", 9093))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        conn.recv(16384)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        file = open("index.html", "r")
        body = file.read()
        resp = response_type + headers + body
        conn.send(resp.encode("utf-8"))
        file.close()
        conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
```

## Task 4
Многопользовательский чат на протоколе `TCP` с использованием библиотеке `threading`.
Логика работы:

* Когда клиент подключается к серверу, то он попадает в список пользователей, который являются экземплярами класса 
`Client`, который состоит из подключения пользователя и его имени;
  
* При первом подключении сервер отправляет клиенту условный `NICKNAME` и ждёт от него ответ, который будет его именем;
  
* Как только сервер получает ответ на `NICKNAME`, пользователь заносится в список. Сам пользователь запускает два треда:
`receive` и `write`. Первая функция принимает сообщения от других юзеров (фактически от сервера), а также завершает работу,
  если сервер выслал ключевое слово `END`. Вторая просто высылает данные серверу — кто и что написал в чат.
  
* У сервера есть две основные функции: `broadcast` и `handle`. Первая рассылает полученное сообщение всем клиентам, кроме отправителя.
Вторая проверяет статус клиента, и если получает ключевое слово `EXIT`, то отключает клиента.

<br>

* `client.py`
``` python
import socket, threading, os, time


def receive():
    try:
        while alive:
            message = sock.recv(1024).decode()
            if message == "NICKNAME":
                sock.send(nickname.encode())
            elif message == "END":
                print("\nThe chat is closed")
                os._exit(1)
            else:
                print(message)
    except KeyboardInterrupt:
        return


def write():
    try:
        while alive:
            message = "{}: {}".format(nickname, input(""))
            sock.send(message.encode())
    except KeyboardInterrupt:
        return


def kill_session():
    sock.send("EXIT".encode())
    sock.close()


def main():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

    data = sock.recv(1024)
    print(data.decode())

    while True:
        pass


if __name__ == "__main__":
    alive = True
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(("localhost", 9094))

    nickname = input("Username: ")

    try:
        main()
    except KeyboardInterrupt:
        alive = False
        sock.send("EXIT".encode())
        print("\nYou left!")
        os._exit(1)
```

* `server.py`
``` python
import socket, threading, os


class Client:
    def __init__(self, connection, username):
        self.connection = connection
        self.username = username


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.connection.send(message)
            except socket.error:
                client.connection.close()
                clients.remove(client)


def handle(client):
    while True:
        message = client.connection.recv(1024)
        if message == b"EXIT":
            client.connection.close()
            clients.remove(client)
            broadcast("{} left!".format(client.username).encode(), client)
            break
        else:
            broadcast(message, client)


def main():
    while True:
        conn, addr = sock.accept()
        print("Connected with {}".format(str(addr)))

        conn.send("NICKNAME".encode())

        clients.append(Client(conn, conn.recv(1024).decode()))
        broadcast("{} joined!".format(clients[-1].username).encode(), conn)
        thread = threading.Thread(target=handle, args=(clients[-1],))
        thread.start()


if __name__ == "__main__":
    clients = []

    sock = socket.socket()
    sock.bind(("localhost", 9094))
    sock.listen(5)

    try:
        main()
    except KeyboardInterrupt:
        broadcast(b"END", sock)
        os._exit(1)
```

## Task 5
Простой web-сервер для обработки `GET` и `POST`.
Сервер может:

* Принять и записать информацию о дисциплине и оценке по дисциплине. В виде `POST` запроса, например, `.../api?name=test&mark=5`.
  
* Отдать информацию обо всех оценках по дисциплине в виде html-страницы.

Всё это реализовывается с помощью обработки `http` запросов, где помогает библиотека `urllib.parse`. 
Каждый предмет — экземпляр класса `Subject`, который состоит из названия предмета и списка оценок по нему. 
Новую оценку можно добавить через функцию `add_mark`.

<br>

* `server.py`
``` python
import socket
from request import Request
from response import Response
from subject import Subject


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.subjects = [Subject("Test Subject", [5, 4, 3])]

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
        try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        except Exception as e:
            print(e)
        client.close()

    def parse_request(self, data):
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(
            method=method, target=target, version=ver, headers=headers, data=data
        )

    def parse_headers(self, req):
        headers = [h for h in req[1 : req[1:].index("") + 1]]
        header_dict = {}
        for header in headers:
            key, value = header.split(":", 1)
            header_dict[key] = value
        return header_dict

    def handle_request(self, req):
        try:
            if req.method == "GET" and req.path == "/":
                return self.handle_root()

            elif req.method == "POST" and req.path.startswith("/api"):
                name = str(req.query["name"][0])
                value = int(req.query["mark"][0])
                for subject in self.subjects:
                    if subject.name == name:
                        subject.add_mark(value)
                        return self.handle_root()
                self.subjects.append(Subject(name, [value]))
                return self.handle_root()

            return self.get_error(404, "Error 404: Not Found")
        except Exception as e:
            print(f"ERROR: {e}")
            return self.get_error(500, e)

    def send_response(self, client, res):
        client.sendall(
            f"HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}".encode()
        )

    def handle_root(self):
        body = """<!DOCTYPE html><html lang="en"><head>"""
        body += (
            """<meta charset="UTF-8"><title>Super Cool Page</title></head><body><table>"""
        )
        body += f"<thead><tr><th>Subject</th><th>Marks</th></tr></thead><tbody>"
        for subject in self.subjects:
            body += f"<tr><td>{subject.name}</td><td>{', '.join(str(x) for x in subject.marks)}</td></tr>"
        body += """</tbody></table>"""
        body += """</body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)

    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == "__main__":
    MyHTTPServer("localhost", 9095, "example.com").serve_forever()
```

* `request.py`
``` python
from urllib.parse import parse_qs, urlparse

class Request:
    def __init__(self, method, target, headers, version, data):
        self.method = method
        self.target = target
        self.version = version
        self.url = urlparse(self.target)
        self.query = parse_qs(self.url.query)
        self.path = self.url.path
        self.headers = headers
        self.data = data
```

* `respose.py`
``` python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```

* `subject.py`
``` python
class Subject:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def add_mark(self, mark):
        self.marks.append(mark)
```