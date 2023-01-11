# Лабораторная работа №1 

## Задача 1

* `server.py`
```python
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send('Hello, client.'.encode('utf-8'))
    print(data.decode('utf-8'))
conn.close()
```
* `client.py`
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))
sock.send('Hello, server.'.encode('utf-8'))

data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()
```

## Задача 2 
* `server.py`
```python
import socket
from math import sqrt

s = socket.socket()

s.bind(('localhost', 9090))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    list_of_coef = data.decode('utf-8').split(',')

    discr = float(list_of_coef[1]) ** 2 - 4 * float(list_of_coef[0]) * float(list_of_coef[2])

    if discr > 0:
        result = 'Корни квадратного уравнения: ' + \
                 str(round((-float(list_of_coef[1]) + sqrt(discr)) / (2 * float(list_of_coef[0])), 2)) + ' ' + \
                 str(round((-float(list_of_coef[1]) - sqrt(discr)) / (2 * float(list_of_coef[0])), 2))
        conn.send(result.encode('utf-8'))
    elif discr == 0:
        result = 'Корень квадратного уравнения: ' + str(round(-float(list_of_coef[1]) / (2 * float(list_of_coef[0])), 2))
        conn.send(result.encode('utf-8'))
    else:
        conn.send('Дискриминант меньше 0. Нет решений'.encode('utf-8'))
conn.close()

```
* `client.py`
```python
import socket

s = socket.socket()
s.connect(('localhost', 9090))

print('Введите коэффициенты квадратного уравнения')

a, b, c = map(float, input().split())
s.send((str(a) + ',' + str(b) + ',' + str(c)).encode('utf-8'))

answer = s.recv(1024)
print(answer.decode('utf-8'))

s.close()
```

## Задача 3 

* `server.py`
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 2468))
server.listen()

while True:
    connection, address = server.accept()
    page = open("index.html")
    info = page.read()
    page.close()
    data = "HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n" + info
    connection.sendto(data.encode("utf-8"), address)
    break

connection.close()
```
* `client.py`
```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2468))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()
```
* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h1>Hello, client!</h1>
</body>
</html>tml>
```

## Задача 4 

* `server.py`
```python
import socket
import threading

host = "localhost"
port = 2465
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
        broadcast(message, client)


def receive():
    while True:
        connection, address = server.accept()
        message = "What's your username?"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192).decode("utf-8")
        users.append(user)
        clients.append(connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()
```

* `client.py`
```python
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 2465))
user = input("Enter your name: ")


def receiving_message():
    while True:
        message = client.recv(8192)
        message = message.decode("utf-8")
        if message == "What's your username?":
            client.sendto(user.encode("utf-8"), ("localhost", 2467))
        else:
            print(message)


def sending_message():
    while True:
        text = input("")
        message = (f"{user}: {text}")
        client.sendto(message.encode("utf-8"), ("localhost", 2467))


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()
```
## Задача 5 

* `server.py`
```python
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
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
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
        try:
            data = client.recv(4096).decode("utf-8")
            request = self.parse_request(data)
            result = self.handle_request(request)
            self.send_response(client, result)
        except Exception as e:
            print('Client serving failed', e)
        client.close()

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
        for course_name in self.marks:
            body += f"<div><span>{course_name}: {self.marks[course_name]}</span></div>"
        second_settings = "</body></html>"
        body += second_settings
        body = body.encode("utf-8")
        headers = [("Content-Type", type),
                   ("Content-Length", len(body))]
        return Response(200, "OK", headers, body)

    def handle_post(self, request):
        course = request["data"]["course"]
        points = request["data"]["points"]

        if course not in self.marks:
            self.marks[course] = []

        self.marks[course].append(points)

        return self.handle_get()

    def send_response(self, connection, response):
        file = connection.makefile('wb')
        status_line = f"HTTP/1.1 {response.status} {response.reason}\r\n"
        status_line = status_line.encode("utf-8")
        file.write(status_line)

        if response.headers:
            for (key, value) in response.headers:
                header_line = f"{key}: {value}\r\n"
                file.write(header_line.encode("utf-8"))

        file.write(b"\r\n")

        if response.body:
            file.write(response.body)

        file.flush()
        file.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 1405
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
```