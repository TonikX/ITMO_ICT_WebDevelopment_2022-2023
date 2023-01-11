# Лабораторная работа №1

## Задание №1

* `server.py`
```python
import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data.decode())
    conn.send(b'hello, client!')

conn.close()
```

* `client.py`
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

sock.send(b'hello, server!')

data = sock.recv(1024)
sock.close()

print(data.decode())
```

## Задание №2
* `server.py`
```python
import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    data = data.decode()
    data = data.split(',')
    a = data[0]
    b = data[1]
    h = data[2]

    S = 0.5 * (int(a) + int(b)) * int(h)
    print(S)

    conn.send(str(S).encode())

conn.close()
```

* `client.py`
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

print('Поиск площади трапеции')
a = input('Введите длину верхнего основания: ')
b = input('Введите длину нижнего основания: ')
h = input('Введите длину высоты: ')

sock.send((a + ',' + b + ',' + h).encode())

data = sock.recv(1024)
sock.close()

print('Площадь трапеции равна: ', data.decode())
```

## Задание №3
* `server.py`
```python
import socket

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
    fin = open('index.html')
    content = fin.read()
    fin.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.send(response.encode())

    conn.close()
```

* `client.py`
```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

data = sock.recv(1024)
sock.close()

print(data.decode())
```

* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>lol</title>
</head>
<body>
    <p>hello, world</p>
</body>
</html>
```

## Задание №4
* `server.py`
```python
import socket
import threading

sock = socket.socket()
sock.bind(('localhost', 9090))
sock.listen(10)

print('[ Server Started ]')

clients = []


def send_messages(msg, author):
    for client in clients:
        if author != client:
            client.send(msg)


def accept_messages(client):
    while True:
        msg = client.recv(1024)
        send_messages(msg, client)


while True:
    try:
        client_socket, address = sock.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=accept_messages, args=(client_socket,))
        thread.start()
    except KeyboardInterrupt:
        print('[ Server stopped ]')
        break
sock.close()
```

* `client.py`
```python
import socket
import threading

sock = socket.socket()
sock.connect(('localhost', 9090))

username = input('Name: ')

def accept_from_server():
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

thread = threading.Thread(target=accept_from_server)
thread.start()


while True:
    try:
        message = input()
        sock.sendall(('[' + username + '] :: ' + message).encode())
    except:
        sock.sendall('Error'.encode())
        print('Error. Disconnected')
        break
sock.close()
```

## Задание №5
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
    serv = MyHTTPServer('127.0.0.1', 9090)
    serv.serve_forever()
```