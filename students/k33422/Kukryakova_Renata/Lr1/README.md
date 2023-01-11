# Отчет по лабораторной работе 1
## _Работа с сокетами_


### Задание 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP

- server1

```sh
import socket

s = socket.socket()
s.bind(('127.0.0.1', 8888))
s.listen(1)
conn, addr = s.accept()
data = conn.recv(1024)
conn.send('Hello, client!'.encode())
print(data.decode('utf-8'))
conn.close()
```

- client1

```sh
import socket

conn = socket.socket()
conn.connect(('127.0.0.1', 8888))
conn.send('Hello, server!'.encode())
data = conn.recv(1024)
print(data.decode('utf-8'))
conn.close()
```
### Задание 2

Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Вариант поиск площади трапеции.

- server2
```sh
import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8888))
sock.listen(10)

conn, addr = sock.accept()
a = int(conn.recv(1024).decode('utf-8'))
b = int(conn.recv(1024).decode('utf-8'))
h = int(conn.recv(1024).decode('utf-8'))
s = (((a+b)/2)*h)
data = str(s)

conn.send(data.encode("utf-8"))
conn.close()
```
- client2
```sh
import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 8888))

a = input("Введите значение верхнего основания трпаеции: ").encode('utf-8')
sock.send(a)
b = input("Введите значение нижнего основания трапеции: ").encode('utf-8')
sock.send(b)
h = input("Введите значение высоты трапеции: ").encode('utf-8')
sock.send(h)

s = sock.recv(1024)
print(s.decode("utf-8"))
sock.close()
#.encode('utf-8')
```
### Задание 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

- server3
```sh
import socket

port = 8888
host = "localhost"

sock = socket.socket()
sock.bind((host, port))

sock.listen(10)
sock, addr = sock.accept()
sock.recv(1024)

response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
page = open('index.html','r')
body = page.read()
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
page.close()
sock.close()
```
- client3
```sh
import socket
sock = socket.socket()
sock.connect(('127.0.0.1', 8888))
sock.send('Hello, server'.encode("utf-8"))
s = sock.recv(1024)
print(s.decode("utf-8"))
sock.close()
```
- index.html
```sh
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>Сайт</title>
  <style>
    {
      background: #F2F2F2;
      max-width: 900px;
      margin: 10px auto;
      padding: 30px;
    }
    h1{
      color: #4C4C4C;
      padding-bottom: 20px;
      margin-bottom: 20px;
      border-bottom: 2px solid #BEBEBE;
    }

  </style>
</head>
<body>
<h1>Урок 1</h1>
  <form action="/add_lesson">

    <input type="text" name="name">
    <textarea rows="10" cols="10" name="description"></textarea>
    <input type="text" name="video_url">
    <input type="submit">
  </form>
</body>
</html>



```

### Задание 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

- server4
```sh
import socket
import threading

server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()

clients = []


def client_thread(client):
    while True:
        msg = client.recv(1024)
        mail_all(msg, client)


def mail_all(msg, current_client):
    for client in clients:
        client.send(msg)


while True:
    client, addr = server.accept()
    print(f'Новый клиент по адресу {addr}')
    client.send('Connected to server!'.encode('utf-8'))

    clients.append(client)

    threading.Thread(target=client_thread, args=(client,)).start()
```

- client4
```sh
import socket
import threading

conn = socket.socket()
conn.connect(('127.0.0.1', 8888))

username = input('Придумайте имя пользователя: ')


def receiver():
    while True:
        print(conn.recv(1024).decode())


def sender():
    while True:
        message = '{}: {}'.format(username, input(''))
        conn.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receiver)
receive_thread.start()

write_thread = threading.Thread(target=sender)
write_thread.start()


```

### Задание 5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Принять и записать информацию о дисциплине и оценке по дисциплине.
Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

- server5
```sh
import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.surnames = []
        self.grades = []
        self.subjects = []

    def serve_forever(self):

        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        data = conn.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(conn, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                resp = "HTTP/1.1 200 OK \n\n"
                with open('grades.html', 'r') as file:
                    resp += file.read()
                return resp

            if method == 'POST':
                resp = "HTTP/1.1 204 OK \n\n"

                parameter = body.split('&')
                for par in parameter:
                    if par.split('=')[0] == 'surname':
                        self.surnames.append(par.split('=')[1])
                    if par.split('=')[0] == 'subject':
                        self.subjects.append(par.split('=')[1])
                    if par.split('=')[0] == 'grade':
                        self.grades.append(par.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, g in zip(self.surnames, self.subjects, self.grades):
                    resp += f"<li>Surname: {s}, Subject: {s}, Grade: {g}</li>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8888
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass
```
- journal.html
```sh
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Журнал</title>
</head>
<body>
<p><h1>Введите оценки</h1>
        <form action="/" method="post">
            <label for="surname">Фамилия:</label>
            <input type="text" name="surname" id="surname"/>
            <label for="subject">Предмет:</label>
            <input type="text" name="subject" id="subject"/>
            <label for="grade">Оценка:</label>
            <input type="number" name="grade" id="grade"/>
            <button>Send</button>
        </form>
    </p>
</body>
</html>
```




