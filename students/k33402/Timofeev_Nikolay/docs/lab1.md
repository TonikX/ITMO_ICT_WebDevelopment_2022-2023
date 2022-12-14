# Лабораторная работа 1

## Пункт 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP

### Клиент

```python
import socket
from loguru import logger


host: tuple[str, int] = ("localhost", 8765)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host)
logger.debug(f"Connecting to socket-server at {host}")
sock.send(b"Hello server\n")

data = sock.recv(24000)
logger.info(f"Server response: {data.decode('utf-8')}")
sock.close()

```

### Сервер

```python
import socket
from loguru import logger

host: tuple[str, int] = ("localhost", 8765)

sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind(host)
    sock.listen(10)
    client_socket, address = sock.accept()
    logger.debug(f"Accepted connection:\n{address}")
    data: bytes = client_socket.recv(24000)
    logger.info(f"User data: {data.decode('utf-8')}")
    client_socket.send(b"Hello client\n")
except Exception as e:
    logger.warning(e)
finally:
    logger.debug("Server stopped")
    sock.close()
```

## Пункт 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Варианты:

a. Теорема Пифагора

b. Решение квадратного уравнения.

c. Поиск площади трапеции.

d. Поиск площади параллелограмма.

Мой вариант: **Теорема Пифагора**

### Клиент

```python
import socket
from loguru import logger

host: tuple[str, int] = ("localhost", 8765)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(host)

for _ in range(2):
    data = sock.recv(24000)
    text = data.decode()
    logger.info("Server response: %s", text)
    side = input()
    sock.send(side.encode())

data = sock.recv(24000)
c_side = data.decode()
logger.info('side is %s', c_side)
sock.close()
```

### Сервер

```python
import socket

from loguru import logger

host: tuple[str, int] = ("localhost", 8765)


def pythagoras_theorem(a: int, b: int) -> float:
    return round((a**2 + b**2) ** (1 / 2))


sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind(host)
    sock.listen(10)
    client_socket, address = sock.accept()
    logger.debug("Connection from %s", address)

    client_socket.send(b"Calculate C side of triangle using Pythagoras theorem. Enter a side:")
    data = client_socket.recv(24000)
    a_side = int(data.decode())

    client_socket.send(b"Enter b side:")
    data = client_socket.recv(24000)
    b_side = int(data.decode())
    client_socket.send(f"C side is: ~{pythagoras_theorem(a=a_side, b=b_side)}".encode())
except Exception as e:
    logger.warning(e)
finally:
    logger.debug("Server stopped")
    sock.close()
```

## Пункт 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

### Клиент

Просто переходим в браузере на [http://localhost:2000](http://localhost:2000)

### Сервер

```python
import socket


class HTTPServer:
    def __init__(self, host: str, port: int, name: str) -> None:
        self._host, self._port = host, port
        self._name: str = name
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def serve_forever(self) -> None:
        try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, address = self._server.accept()
                self._serve_client(client)
        except KeyboardInterrupt:
            self._server.close()

    def _serve_client(self, client) -> None:
        html = self._handle_request()
        self._send_response(client, html)

    @staticmethod
    def _handle_request(filename: str = 'index.html') -> str:
        with open(filename, "r") as file:
            body = file.read()
        return body

    @staticmethod
    def _send_response(client: socket.socket, document: str) -> None:
        client.sendall(
            f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{document}'.encode()
        )


if __name__ == '__main__':
    host = ('127.0.0.1', 2000)
    print(f'server started at http://{host[0]}:{host[1]}')
    HTTPServer(*host, 'example.com').serve_forever()
```

## Пункт 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

### Клиент

```python
import socket
import sys
import threading
import uuid

from loguru import logger

logger_format = (
    "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
    "<level>{level}</level> | "
    "<level>{message}</level>"
)
logger.remove()
logger.add(sys.stdout, format=logger_format)


class ChatClient:
    def __init__(self, ip: str, port: int):
        self._alias = f"Anonymous_{uuid.uuid1().hex[:5]}"
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.connect((ip, port))

    def _receive(self):
        while True:
            try:
                message = self._sock.recv(1024).decode()
                logger.info(message)
            except Exception as e:
                logger.info("Disconnected from server")
                break
        self._sock.close()

    def _send(self):
        while True:
            message = input()
            if message == '/quit':
                break
            self._sock.send(message.encode())
        self._sock.close()

    def start(self):
        try:
            self._sock.send(self._alias.encode())

            receive_thread = threading.Thread(target=self._receive)
            receive_thread.start()

            send_thread = threading.Thread(target=self._send)
            send_thread.start()
        except Exception:
            logger.warning("Something went wrong")


if __name__ == "__main__":
    ChatClient("127.0.0.1", 9095).start()
```

### Сервер

```python
import socket, threading

from loguru import logger


class ChatServer:
    def __init__(self, ip: str, host: int):
        self._sock: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((ip, host))
        self._sock.listen()
        self._clients: dict[socket.socket, str] = {}

    def _broadcast(self, message: str):
        for client in self._clients.keys():
            client.send(message.encode())

    def _handle_client(self, client: socket.socket):
        while True:
            try:
                message = client.recv(1024).decode()
                if message == '/quit' or not message:
                    client.close()
                else:
                    self._broadcast(f"{self._clients[client]}: {message}")
            except Exception as e:
                msg = f'{self._clients[client]} left chat'
                client.close()
                self._clients.pop(client)
                self._broadcast(msg)
                logger.info(msg)
                break

    def _receive(self):
        logger.info(f"Server working on {self._sock.getsockname()}")

        while True:
            client, address = self._sock.accept()
            logger.info(f"{str(address)} connected!")
            alias = client.recv(1024).decode()
            self._clients[client] = alias
            self._broadcast(f"{alias} connected. Send /quit to disconnect")
            thread = threading.Thread(target=self._handle_client, args=(client,))
            thread.start()

    def run(self):
        try:
            self._receive()
        except KeyboardInterrupt:
            logger.critical("Server stopped by sigterm")


if __name__ == "__main__":
    ChatServer("127.0.0.1", 9095).run()
```

## Пункт 5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:
● Принять и записать информацию о дисциплине и оценке по дисциплине.
● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

### Клиент

Переходим в браузере на localhost

### Сервер

```python
import socket
from utils import Request, Response
from urllib.parse import parse_qs
from email.parser import BytesParser


class BaseHTTPServer:
    def __init__(self, host: str, port: int, name: str) -> None:
        self._host = host
        self._port = port
        self._name = name
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def handle_request(self, req):
        raise NotImplementedError

    def handle_root(self):
        raise NotImplementedError

    def serve_client(self, client) -> None:
        try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        except Exception as e:
            print(e)
        client.close()

    def serve_forever(self) -> None:
        try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, address = self._server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            self._server.close()
    
    def parse_request(self, data) -> Request:
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    @staticmethod
    def parse_headers(req) -> dict[str, str]:
        headers = list(req[1:req[1:].index("") + 1])
        headers_dict = {}
        for h in headers:
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    @staticmethod
    def send_response(client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    def _generate_error(self, code: int, text: str) -> Response:
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


class MyHTTPServer(BaseHTTPServer):
    def __init__(self, host: str, port: int, name: str) -> None:
        super().__init__(host, port, name)
        self._marks: dict[str, str] = {
            "Math": "2",
            "Linux": "3",
            "OOP": "2",
            "SQL": "2",
            "Physics": "5",
            "Web-Programming": "4"
        }

    def handle_root(self):
        body = """<!DOCTYPE html><html><head>"""
        with open("style.css", "r") as file:
            body += f"<style>{file.read()}</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += "<thead><tr><th>ID</tр><th>Subject</th><th>Score</th></tr></thead><tbody>"
        for i, mark in enumerate(self._marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)


    def handle_request(self, req):
        try:
            match req.method:
                case 'GET':
                    if req.path == "/":
                        return self.handle_root()
                    return self._generate_error(404, 'page not found')
                case 'POST':
                    if req.path.startswith("/api"):
                        subject_id = int(req.query["id"][0]) - 1
                        value = int(req.query["value"][0])
                        if value not in range(1, 6):
                            raise ValueError("Score must be between 1, 2, 3, 4 or 5")
                        self._marks[list(self._marks.keys())[subject_id]] = str(value)
                        return self.handle_root()
                    if req.path.startswith("/form-request"):
                        query = parse_qs(req.data[-int(req.headers["Content-Length"]):])
                        _id = int(query["id"][0]) - 1
                        value = int(query["value"][0])
                        if value not in range(1, 6):
                            raise ValueError("Score must be between 1, 2, 3, 4 or 5")
                        self._marks[list(self._marks.keys())[_id]] = str(value)
                        return self.handle_root()
                case _:
                    return self._generate_error(405, "Method not allowed")
        except Exception as e:
            print(f"Exception: {e}")
            return self._generate_error(500, str(e))


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2007, 'example.com').serve_forever()
```

