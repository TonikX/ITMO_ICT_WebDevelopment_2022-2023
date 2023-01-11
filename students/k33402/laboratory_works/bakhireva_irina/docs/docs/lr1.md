# Лабораторная работа 1
## _Работа с сокетами_


### Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP

- task_1/server.py

```python
import socket

sock = socket.socket()
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

client, address = sock.accept()
msg = client.recv(1024)
print(msg.decode("utf-8"))
client.send(b"Hello, client!")
sock.close()
```

- task_1/client.py

```python
import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 9090))
sock.send(b"Hello, server!")

msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()
```
### Задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Вариант поиск площади параллелограмма.

- task_2/server.py
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

while True:
    client, address = sock.accept()
    s = int(client.recv(1024).decode())
    h = int(client.recv(1024).decode())
    result = str(s*h)
    client.send(result.encode())

```
- task_2/client.py
```python
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 9090))
s = input("Enter the base:")
h = input("Enter the height:")
sock.send(s.encode())
sock.send(h.encode())

msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()
```
### Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

- task_3/server.py
```python
import socket

sock = socket.socket()
sock.bind((socket.gethostname(), 9090))
sock.listen(1)

client, address = sock.accept()
client.sendall(b"HTTP/1.0 200 OK\nContent-Type: text/html\n\n" + open('index.html', 'rb').read())
msg = client.recv(1024)

client.close()
```
- task_3/client.py
```python
import socket

sock = socket.socket()
sock.connect((socket.gethostname(), 9090))

msg = sock.recv(1024)
print(msg.decode("utf-8"))

sock.close()
```
- task_3/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Task 3</title>
</head>
<body>
    <h1>Всем привет!</h1>>
</body>
</html>
```

### Задание 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

- task_4/server.py
```python
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))
sock.listen(10)
users = set()


def connecting_users():
    while True:
        client, address = sock.accept()
        users.add(client)
        print('User connected:' + str(address))
        cl_add = threading.Thread(target=msg, args=[client, address])

        cl_add.start()


def msg(client, address):

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print('info:', data)
            if not data:
                break
            for user in users:
                if user == client:
                    continue
                user.sendall(data.encode('utf8'))
        except Exception:
            users.remove(client)

            break
    print('User have closed chat: ' + str(address))
    client.close()


cnx = threading.Thread(target=connecting_users())
cnx.start()
```

- task_4/client.py
```python
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
name = input('Enter your name: ')


def send_message():
    try:
        while True:
            msg = input()
            sock.sendall(bytes(name + ": " + msg, "utf-8"))
            if msg == "Пока":
                sock.close()
                break
    except Exception:
        pass


def receive_message():
    try:
        while True:
            data = sock.recv(1024).decode("utf-8")
            if not data:
                break
            print(data)
        sock.close()
    except Exception:
        pass


send = threading.Thread(target=send_message)
receive = threading.Thread(target=receive_message)

send.start()
receive.start()
```

### Задание 5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Принять и записать информацию о дисциплине и оценке по дисциплине.
Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

- task_5/server.py
```python
import socket


class MyHTTPServer:

    # Server parameters
    def __init__(self, host, port):
        self._host = host
        self._port = port

    # Starting the server on a socket, processing incoming connections
    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        try:
            sock.bind((self._host, self._port))
            sock.listen()
            while True:
                conn, _ = sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            sock.close()

    # Processing client connection
    def serve_client(self, conn):
        data = conn.recv(18456)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        self.send_response(conn, resp)

    # Processing request
    def parse_request(self, msg):
        msg = msg.replace('\r', '')
        req_line = msg.split('\n')
        method, target, protocol = req_line[0].split()
        return target, method

    # Processing headers
    def parse_headers(self, msg):

        msg = msg.replace('\r', '')
        hd_line = msg.split('\n')
        i = hd_line.index('')
        hd = hd_line[1:i]
        body = hd_line[-1]
        return hd, body

    # A function for processing the url according to the desired method.
    # The GET request should return data. The POST request should record data based on the passed parameters.

    def handle_request(self, target, method, body):
        if target == "/":
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


            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

    # Sending a response
    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    subjects = []
    marks = []

    serv = MyHTTPServer('localhost', 9091)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
- task_5/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JOURNAL</title>
    <style>
        .left-aligned {
            float: left;
            color: blue;
            padding: 15px;
        }

        .right-aligned {
            float: right;
            color: blue;
            padding: 15px;
        }
    </style>
</head>
<body style="background-color:grey;text-align:center">


<form id='input-form' action='' method='POST'>
    <div>
        <span class='left-aligned'>Bakhireva Irina</span>
        <span class='right-aligned'>Group K33402</span>
        <label for="name"><p>Subject</label>
        <input type="text" id="name" name="subject"/>
    </div>
    <div>
        <label for="mail"><p>Mark </label>
        <input type="number" id="mail" name="mark"/>
    </div>
    <div>
        <input type="submit" value="Submit">
        <input type="reset" value="Reset">
    </div>
</form>
</body>
</html>
```



