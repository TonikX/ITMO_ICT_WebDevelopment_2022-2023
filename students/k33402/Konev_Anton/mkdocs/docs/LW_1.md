# Лабораторная работа №1

## Задача №1

* `server.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8071))
sock.listen(5)
client_socket, addr = sock.accept()
print(client_socket.recv(1024).decode("utf-8"))
client_socket.send(b"Hello, client")
sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8071))
sock.send(b"Hello, server")
print(sock.recv(1024).decode("utf-8"))
sock.close()
```

## Задача №2

* `server.py`

```python
import math
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8091))
sock.listen(10)
client_socket, addr = sock.accept()
client_socket.send(b"Hello, client\nPlease enter the coefficients a, b, c of your equation like ax^2+bx+c=0")
coefs = client_socket.recv(1024).decode("utf-8")
'''
https://younglinux.info/python/task/quadratic
'''
a = float(coefs[0])
b = float(coefs[2])
c = float(coefs[4])
discr = b ** 2 - 4 * a * c

if discr < 0:
    msg = "No real roots"
elif discr == 0:
    x = -b / (2 * a)
    msg = "x = %.2f" % x
else:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    msg = "x1 = %.2f \nx2 = %.2f" % (x1, x2)

client_socket.send(msg.encode("utf-8"))
sock.close()
```

* `client.py`

```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 8091))
print(sock.recv(1024).decode("utf-8"))
coefs = input("Enter a, b, c divided by space: ").encode("utf-8")
sock.send(coefs)
print(sock.recv(1024).decode("utf-8"))
sock.close()
```

## Задача №3

* `server.py`

```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('127.0.0.1', 8901))
conn.listen(10)

while True:
    try:
        client_socket, addr = conn.accept()
        client_socket.recv(1024)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        f = open("index.html", "r")
        body = f.read()
        res = response_type + headers + body
        client_socket.send(res.encode("utf-8"))
        f.close()
        client_socket.close()
    except KeyboardInterrupt:
        conn.close()
        break
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Main</title>
</head>
<body>
<h1>Hello, client</h1>
</body>
</html>
```

## Задача №4

* `server.py`

```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(('127.0.0.1', 8902))

clients = []
while True:
    try:
        data, client_address = conn.recvfrom(1024)
        if client_address not in clients:
            clients.append(client_address)
        for client in clients:
            if client != client_address:
                conn.sendto(data, client)
    except KeyboardInterrupt:
        conn.close()
        break

```

* `client.py`

```python
import socket
import threading

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(('127.0.0.1', 8902))


def messages():
    while True:
        data = conn.recv(2048)
        print(data.decode("utf-8"))


def chat():
    name = input("Enter your name: ")
    print(f'{name}, say hello to the chat')
    conn.sendall(bytes(f"{name} joined", "utf-8"))
    while True:
        conn.sendto(bytes(f"{name}: {input()}", "utf-8"), ('127.0.0.1', 8902))


thread1, thread2 = threading.Thread(target=messages), threading.Thread(target=chat)
thread1.start(), thread2.start()
```

## Задача №5

* `server.py`

```python
import socket


class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(5)
        while True:
            clientsocket, _ = sock.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(16384)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, target, protocol = lines[0].split()
        return target, method

    def parse_headers(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        i = lines.index('')
        headers = lines[1:i]
        body = lines[-1]
        return headers, body

    def handle_request(self, target, method, body):
        if target == "/":
            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

            if method == "POST":
                newbody = body.split('&')
                for a in newbody:
                    if a.split('=')[0] == 'subject':
                        subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        marks.append(a.split('=')[1])

                resp = "HTTP/1.1 200 OK\n\n"
                resp += "<html><head><title>Journal</title></head><body>"
                for s, m in zip(subjects, marks):
                    resp += f"<p>{s}: {m}</p>"
                resp += "</body></html>"
                return resp

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = 'localhost'
    port = 9090
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Journal</title>
</head>
<body>
<form action="/" method="post">
    <div>
        <label for="name">Subject:</label>
        <input type="text" id="name" name="subject"/>
    </div>
    <div>
        <label for="mail">Mark:</label>
        <input type="number" id="mail" name="mark"/>
    </div>
    <div>
        <input type="submit">
    </div>

</body>
</html>
```

