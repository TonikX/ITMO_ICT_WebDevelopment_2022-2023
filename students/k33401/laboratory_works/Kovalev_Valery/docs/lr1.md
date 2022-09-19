# Лабораторная работа 1

## Задача 1

* `server.py`
```python
import socket


def server():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"{data.decode('utf-8')} from {addr[0]}:{addr[1]}")
        conn.send(str.encode(f"Hello, {addr[0]}:{addr[1]}"))

    conn.close()


if __name__ == "__main__":
    server()
```

* `client.py`
```python
import socket


def client():
    sock = socket.socket()
    sock.connect(('127.0.0.1', 9090))
    sock.send(b'Hello, server!')

    data = sock.recv(1024)
    sock.close()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    client()
```

## Задача 2

* `server.py`
```python
import socket


def pythagorean_theorem(a, b):
    return a * a + b * b


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 9091))
    sock.listen()
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    a = ""
    b = ""
    result = ""

    while not result:
        while not a:
            conn.send("Side A".encode())
            data = conn.recv(1024).decode()
            if data.isdigit():
                a = float(data)

        while not b:
            conn.send("Side B".encode())
            data = conn.recv(1024).decode()
            if data.isdigit():
                b = float(data)

        result = pythagorean_theorem(a, b)
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
    sock.connect(('127.0.0.1', 9091))
    print("I solve Pythagorean theorem")
    a = ""
    while not a.isdigit():
        a = input("Enter a side A: ")
    b = ""
    while not b.isdigit():
        b = input("Enter a side B: ")

    while True:
        data = sock.recv(1024).decode()
        if data == "Side A":
            sock.send(a.encode())
        if data == "Side B":
            sock.send(b.encode())
        if data.startswith("Result"):
            print(data)
            break


if __name__ == "__main__":
    client()
```

## Задача 3

* `server.py`
```python
import socket


class MyHTTPServer:
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

    def handle_request(self):
        with open("index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, client, html):
        client.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode())


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2000, 'example.com').serve_forever()
```

## Задача 4

* `server.py`
```python
import socket, threading


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
        print("Server has started")
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
    MyChat("127.0.0.1", 9091).run()

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
                if message == "What is your alias?":
                    self.sock.send(self.alias.encode())
                else:
                    print(message)
            except:
                print("Error!")
                self.sock.close()
                break

    def send(self):
        while True:
            message = input()
            self.sock.send(message.encode())

    def start(self):
        self.alias = input("Enter your alias: ")
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()


if __name__ == "__main__":
    MyClient("127.0.0.1", 9091).start()
```

## Задача 5

* `server.py`
```python
import socket
from Request import Request
from Response import Response
from urllib.parse import parse_qs

class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.marks = {"Web-программирование": "1",
                      "Компьютерные сети": "5",
                      "Операционные системы": "1",
                      "Иностранный язык": "1"}

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
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    def parse_headers(self, req):
        headers = [h for h in req[1:req[1:].index("") + 1]]
        hdict = {}
        for h in headers:
            k, v = h.split(':', 1)
            hdict[k] = v
        return hdict

    def handle_request(self, req):
        try:
            if req.method == "GET" and req.path == "/":
                return self.handle_root()
            if req.method == "POST" and req.path.startswith("/api"):
                _id = int(req.query["id"][0]) - 1
                value = int(req.query["value"][0])
                if value > 5 or value < 1:
                    raise Exception("Неверное значение оценки")
                self.marks[list(self.marks.keys())[_id]] = value
                return self.handle_root()
            if req.method == "POST" and req.path.startswith("/form-request"):
                q = parse_qs(req.data[-int(req.headers["Content-Length"]):])
                _id = int(q["id"][0]) - 1
                value = int(q["value"][0])
                if value > 5 or value < 1:
                    raise Exception("Неверное значение оценки")
                self.marks[list(self.marks.keys())[_id]] = value
                return self.handle_root()
            return self.get_error(404, "Ты даже не гражданин!")
        except Exception as e:
            print(f"ERROR: {e}")
            return self.get_error(500, e)

    def send_response(self, client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    def handle_root(self):
        body = """<!DOCTYPE html><html lang="en"><head>"""
        with open("res/style.css", "r") as file:
            body += "<style>"
            body += file.read()
            body += "</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += f"<thead><tr><th>ID</tр><th>Предмет</th><th>Оценка</th></tr></thead><tbody>"
        for i, mark in enumerate(self.marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("res/form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)

    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2001, 'example.com').serve_forever()
```

* `Response.py`
```python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```

* `Request.py`
```python
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