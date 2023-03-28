# Лабораторная работа №1

## Задача №1
Серверная часть приложения
* `server.py`
```python
import socket

host = "localhost"
port = 2468
message = "Hello, client"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
while True:
    received_message, address = server.recvfrom(4096)
    print("Client said: ", received_message.decode("utf-8"))
    server.sendto(message.encode("utf-8"), address)
    server.close()
    break
```
Клиентская часть приложения
* `client.py`
```python
import socket

host = "localhost"
port = 2468
message = "Hello, server"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
client.sendto(message.encode("utf-8"), (host, port))
received_message, address = client.recvfrom(4096)
print("Server said: ", received_message.decode("utf-8"))
client.close()
```

## Задача №2
Серверная часть приложения
* `server.py`
```python
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
        connection.sendto("upper base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        a = float(data)
    while not b:
        connection.sendto("lower base of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        b = float(data)
    while not h:
        connection.sendto("height of the trapezoid".encode("utf-8"), address)
        data = connection.recv(4096)
        data = data.decode("utf-8")
        h = float(data)

    area = 0.5 * (a + b) * h
    connection.sendto(str.encode(f"the area of this trapezoid is {area}", encoding="utf-8"), address)

connection.close()
```
Клиентская часть приложения
* `client.py`
```python
import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
a = input("length of the upper base of your trapezoid: ")
print()
b = input("length of the lower base of your trapezoid: ")
print()
h = input("length of the height of your trapezoid: ")
print()
a = a.encode("utf-8")
b = b.encode("utf-8")
h = h.encode("utf-8")
while not a.isdigit():
    print("this value must be a number")
    print()
    a = input("length of the upper base of your trapezoid: ")
    print()
    a = a.encode("utf-8")
while not b.isdigit():
    print("this value must be a number")
    print()
    b = input("length of the lower base of your trapezoid: ")
    print()
    b = b.encode("utf-8")
while not h.isdigit():
    print("this value must be a number")
    print()
    h = input("length of the height of your trapezoid: ")
    print()
    h = h.encode("utf-8")

while True:
    data = client.recv(4096)
    data = data.decode("utf-8")
    if data == "upper base of the trapezoid":
        client.sendto(a, (host, port))
    if data == "lower base of the trapezoid":
        client.sendto(b, (host, port))
    if data == "height of the trapezoid":
        client.sendto(h, (host, port))
    if data.startswith("The area"):
        print(f"server calculated the area of the trapezoid with the parameters:\n"
              f"    1) length of the upper base of your trapezoid: {float(a)}\n"
              f"    2) length of the lower base of your trapezoid: {float(b)}\n"
              f"    3) length of the height of your trapezoid: {float(h)}\n")
        print(data)
        break

client.close()
```

## Задача №3
Серверная часть приложения
* `server.py`
```python
import socket

class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        address = (self.host, self.port)
        try:
            server.bind(address)
            server.listen()
            while True:
                client, address = server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            server.close()

    def serve_client(self, client):
        html = self.handle_request()
        self.send_response(client, html)
        client.close()

    def handle_request(self):
        with open("task3/index.html", "r") as file:
            body = file.read()
        return body

    def send_response(self, client, html):
        client.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode("utf-8"))


if __name__ == '__main__':
    host = "localhost"
    port = 2468
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
```
HTML страница приложения
* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>greatest kpop groups and artists of all time!</title>
</head>
<body>
  <h1>1st generation</h1>
  <article>
    boa
    <br />
   lee hyori
  </article>
  <h1>2nd generation</h1>
  <article>
    super junior
    <br />
    2ne1
  </article>
  <h1>3rd generation</h1>
  <article>
    nct
    <br />
    red velvet
  </article>
  <h1>4th generation</h1>
  <article>
    ateez
    <br />
    itzy
  </article>
  <h1>honorable mentions</h1>
  <article>
    blackpink
    <br />
    stray kidz
  </article>
</body>
</html>
```
Клиентская часть приложения
* `client.py`
```python
import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()
```
## Задача №5
Серверная часть приложения
* `server.py`
```python
import socket
from response import Response


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.points = {"visualization": ["73", "61", "90", "88"],
                       "mathematics": ["67", "100", "88"],
                       "p.e.": ["61", "55", "73"]}

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
            print("client connection failed: ", exception_text)
        connection.close()

    def parse_request(self, data):
        request = data.rstrip('\r\n')
        text = request[:data.index("\n")].split()
        if len(text) != 3:
            raise Exception("incorrect request line")

        method, target, version = text
        if version != 'HTTP/1.1':
            raise Exception("unexpected HTTP version")

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
        course = "<form><label>discipline name: </label><input name='course' /><br><br>"
        points = "<label>points: </label><input name='points' /><br><br>"
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
            raise Exception("incorrect value! please enter a number between 0 and 103.")
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
        return Response(code, "ok", "Content-Type: text/html; charset=utf-8", text)


if __name__ == '__main__':
    host = 'localhost'
    port = 2468
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
```
Ответ
* `response.py`
```python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```
