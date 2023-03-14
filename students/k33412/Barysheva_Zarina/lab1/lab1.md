# Лабораторная работа №1
## Пункт 1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
### Сервер
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4457))
sock.listen(1)
conn, addr = sock.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(data)
    conn.send('Hello, client!'.encode())

conn.close()
```
### Клиент
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4457))
sock.send('Hello, server!'.encode())

data = sock.recv(1024)
sock.close()

print (data)
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
### Сервер
```
import socket

def pifagor(a: int, b: int) -> float:
    return round((a**2 + b**2) ** (1 / 2))

def square_equation(a: int, b: int, c: int) -> list[float]:
    d = b**2 - 4*a*c
    if (d < 0):
        return []
    if (d == 0):
        x = -b / (2*a)
        return [x]
    x1 = (-b - d**(1/2)) / (2*a)
    x2 = (-b + d**(1/2)) / (2*a)
    return [x1, x2]

def s_trapezoid(a: int, b: int, h: int) -> float:
    return 1/2*a*b*h

def s_parallelogram(a: int, h: int) -> int:
    return a*h

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4462))
sock.listen(1)
conn, addr = sock.accept()

conn.send("Выбери один из вариантов:'\n'1 - теорема Пифагора '\n'2 - решить квадратное уравнение '\n'3 - вычислить площадь трапеции '\n'4 - вычислить площади параллелограмма".encode())

while True:
    data = conn.recv(24000)
    if not data:
        break
    v = int(data.decode())
    match v:
        case 1:
            conn.send("Введите a и b".encode())
            data = conn.recv(24000)
            a, b = map(int, data.decode().split())
            ans = pifagor(a, b)
            conn.send(f'Ответ: {ans}'.encode())
        case 2:
            conn.send("Введите параметры уравнения".encode())
            data = conn.recv(24000)
            a, b, c = map(int, data.decode().split())
            roots = square_equation(a, b, c)
            if roots:
                conn.send(f'Количество корней: {len(roots)}; Ответ: {roots}'.encode())
            else:
                conn.send('Рациональных корней нет'.encode())
        case 3:
            conn.send("Введите основания и высоту".encode())
            data = conn.recv(24000)
            a, b, h = map(int, data.decode().split())
            ans = s_trapezoid(a, b, h)
            conn.send(f'Ответ: {ans}'.encode())
        case 4:
            conn.send("Введите основание и высоту".encode())
            data = conn.recv(24000)
            a, h = map(int, data.decode().split())
            ans = s_parallelogram(a, h)
            conn.send(f'Ответ: {ans}'.encode())
        case _:
            conn.send("Таких вычислений нет'\n'".encode())

conn.close()
```
### Клиент
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4462))


data = sock.recv(24000)
print(data.decode())

v = str(input())
sock.send(v.encode())
data = sock.recv(24000)
print(data.decode())

if(data.decode() != "Таких вычислений нет'\n'"):
    resps = input()
    sock.send(resps.encode())
    data = sock.recv(24000)
    print(data.decode())


sock.close()
```
## Пункт 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.
### Сервер
```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4467))
sock.listen(1)
conn, addr = sock.accept()

with conn:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        with open('index.html', "r") as file:
            html = file.read()
        conn.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html}'.encode())
```
## Пункт 4
Реализовать многопользовательский чат.
### Сервер
```
import socket, threading
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4851))
sock.listen()
users: dict = {}


def send_message(message: str):
    for conn in users:
        author = message.split(" ")[0]
        if author != users[conn]:
            conn.send(message.encode())


def save_user(conn: socket.socket):
    conn.send(b'Enter your name:')
    token = conn.recv(2048).decode("utf-8")
    users[conn] = token
    send_message(f"{token} присоедился к чату!")

    while True:
        message = conn.recv(24000)
        print(f'{token} отправил сообщение: {message.decode("utf-8")}')
        if not message or message == '.q':
            break
        send_message(f'{token} сообщил: {message.decode("utf-8")}')


try:
    while True:
        conn, addr = sock.accept()
        print(f"{conn}, {addr} присоединился к чату")
        thread_user = threading.Thread(target=save_user, args=[conn]).start()
except KeyboardInterrupt:
    print('Stop')
finally:
    sock.close()
```
### Клиент
```
import socket
from threading import Thread


def listen_for_messages():
    while True:
        print(sock.recv(2048).decode('utf-8'))


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4851))

thread = Thread(target=listen_for_messages)
thread.daemon = True
thread.start()

while True:
    message_to_send = input()
    sock.send(message_to_send.encode("utf-8"))
    if message_to_send == '.q':
        sock.close()
        break
```
## Пункт 5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.
Сервер может:
* Принять и записать информацию о дисциплине и оценке по дисциплине.
* Отдать информацию обо всех оценах по дсициплине в виде html-страницы.
### Сервер
```
import socket
 
class MyHTTPServer:
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self._name = name
        self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._marks: dict = {}
 
    def serve_forever(self):
        try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                conn, address = self._server.accept()
                self.serve_client(conn)
        finally:
            self._server.close()
 
    def serve_client(self, conn):
        try:
            data = conn.recv(1024).decode()
            print('get a request')
            reqst = self.parse_request(data)
            print(f'request {reqst}')
            page = self.handle_request(reqst)
            self.send_response(reqst, page, conn)
        finally:
            conn.close()
 
    def parse_request(self, data):
        reqst = data.split("\r\n")
        method, target, version = reqst[0].split(" ")
        headers = self.parse_headers(str(reqst[1:]))
        body = data.split('\r\n\r\n')[1]
        return {'method': method, 'target': target, 'version': version, 'headers': headers, 'data': body}
 
    def parse_headers(self, reqst):
        end_of_headers = reqst.find('\r\n\r\n')
        headers = reqst[:end_of_headers].split('\r\n')
        headers_dict = {}
        for h in headers:
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    def handle_request(self, reqst):
        # try:
            if reqst['method'] == 'POST':
                subject_list = reqst['data'].split('&')
                print(subject_list)
                new_subject = subject_list[0].split('=')[1]
                new_mark = subject_list[1].split('=')[1]
                print(new_mark, new_subject)
                self._marks[new_subject] = new_mark
            return self.generate_page()
        # except Exception:
        #     return '<h1>BadRequest: An error occured.</h1>'
 
    def send_response(self, reqst, page, conn):
        conn.sendall(f"HTTP/1.1 200 OK\r\n{reqst['headers']}\r\n\r\n{page}".encode())
 
    def generate_page(self):
        print('generate html page')
        html = '<!DOCTYPE html><html lang="ru"><head><meta charset="utf-8"><title>Оценки</title></head><body>'
        html += "<table><thead><tr><th>Название предмета</th><th>Оценка</th></tr></thead><tbody>"
        for subject, mark in self._marks.items():
            html += f"<tr><td>{subject}</td><td>{mark}</td></tr>"
        html += "</tbody></table>"
        with open("form.html", "r") as file:
            html += file.read()
        return html
 
if __name__ == '__main__':
    host = 'localhost'
    port = 4560
    name = 'lab5'
    print(f'Running on {host}:{port}')
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```