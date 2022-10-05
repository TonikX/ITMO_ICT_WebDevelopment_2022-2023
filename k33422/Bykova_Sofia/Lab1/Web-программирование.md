# Web-программирование
## Лабораторная работа 1
### Задание 1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP
# Server
```py
import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #_DGRAM - UDP 
s.bind(addr)

while True:
    msg = s.recvfrom(1024)
    message = msg[0].decode('utf-8')
    clientMsg = 'Message from client: {}'.format(message)

print(clientMsg)
s.sendto(str.encode('Hello, client!'))
```
# Client
```py
import socket

s1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
s1.sendto(str.encode('Hello, server!'), ('localhost', 9090)) #отправляем сообщение по адресу
msg = s1.recvfrom(1024)
msgg = 'Message from server: {}'.format(msg[0].decode('utf-8'))
print(msgg)
```
### Задание 2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера выполнение математической операции, параметры, которые вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту. 
Поиск площади трапеции.
# Server
``` py
import socket
import sys

host = 'localhost'
port = 9090
addr = (host, port)

sock_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv.bind(addr)
sock_serv.listen(5)

while True:
    clientsock, address = sock_serv.accept()
    data = clientsock.recv(4096)
    values = data.decode("utf-8")
    values = values.split(" ") # разделяем полученные данные по пробелу
    h = float(values[0])
    s = float(values[1])
    # print(h, s, sep = ' ') для поиска ошибок
    square = h * s
    if square <= 0:  # исключаем невозможные параметры
        clientsock.send((str('Ошибка. Значения не могут быть такими! Проверьте введённые данные.')).encode('utf-8'))
        sys.exit()
    clientsock.send(bytes(str(square), "utf-8"))
```
# Client
``` py
import socket

sock_cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_cli.connect(('localhost', 9090))

h = input("Введите значения высоты и основания параллелограмма -> ")
sock_cli.send(bytes(h.encode('utf-8')))

data = sock_cli.recv(4096)
data = data.decode('utf-8')

print(f'Площадь = {data}')
```
## Задание 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.
# Server
```py
import socket

host = 'localhost'
port = 5002
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(10)


while True:
    conn, address = sock.accept()
    response_type = "/HTTP/1.0 200 OK\n"
    headers = "Content-Type: text/html\n\n"
    file = open('index.html', 'r')
    body = file.read()
    response = response_type + headers + body
    conn.sendall(response.encode('utf-8'))
    conn.close()
```
# Client
```py
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5002))

data = sock.recv(4096)
print(data.decode('utf-8'))
sock.close()
```
# index.html
```
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form action="action_form.php" method="POST">
<p>What genres of music from the list do you like?</p>
<ol>
  <li><input type="checkbox" name="music" value="jazz" >Jazz</li>
  <li><input type="checkbox" name="music" value="blues" >Blues</li>
  <li><input type="checkbox" name="music" value="rock">Rock</li>
  <li><input type="checkbox" name="music" value="shanson">Chanson</li>
  <li><input type="checkbox" name="music" value="country">Country</li>
</ol>
<input type="submit">
</form>
</body>
</html>
```
## Задание 4
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.
# Server
```py
import socket
import threading

host = 'localhost'
port = 5002
addr = (host, port)

clients = []  # список с адресами
nicknames = []  # список с именами
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen()


def broadcast(message):   #отправляем сообщения всем подключённым клиентам
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8')) #уведомляем участников чата, что {nickname} покинул чат
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = sock.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
```
# Client
```py
import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5002))
nickname = input("Введите ваше имя: ")


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'NICK':
                sock.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            sock.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        sock.send(message.encode('utf-8'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
```
## Задание 5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Задание: сделать сервер, который может:
● Принять и записать информацию о дисциплине и оценке по дисциплине.
● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.
# Server
```py
import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
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
                    if par.split('=')[0] == 'subject':
                        self.subjects.append(par.split('=')[1])
                    if par.split('=')[0] == 'grade':
                        self.grades.append(par.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, g in zip(self.subjects, self.grades):
                    resp += f"<li>Subject: {s}, Grade: {g}</li>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8000

    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
# Grades.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>kinda bars</title>
</head>
<body>
<p>Enter data regarding grades
        <form action="/" method="post">
            <label for="subject">Subject:</label>
            <input type="text" name="subject" id="subject"/>
            <label for="grade">Grade:</label>
            <input type="number" name="grade" id="grade"/>
            <button>Send</button>
        </form>
    </p>
</body>
</html>
```


