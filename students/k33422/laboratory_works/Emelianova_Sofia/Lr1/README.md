# README
## Лабораторная работа №1

### _Задание 1:_ Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.
Серверная часть:
``` py
# Импортируем библиотеку socket  
import socket 
# Выбираем сообщение клиенту
mfs = "Hello, client" 
# Кодируем строку
data = str.encode(mfs) 
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#  Связываем сокет с хостом и портом
s.bind((socket.gethostname(), 2222)) 
while True: 
# Получаем данные порциями по 1024 байта
    mes = s.recvfrom(1024) 
# Делим сообщение по индексам 
    message = mes[0] 
    address = mes[1] 
    print(message) 
# Отправляем ответ клиенту 
    s.sendto(data, address)
```
Клиентская часть:
``` py
# Импортируем библиотеку socket  
import socket 
# Выбираем сообщение серверу 
mfc = "Hello, server" 
# Кодируем строку
data = str.encode(mfc)
# Подключаемся к хосту
sad = (socket.gethostname(), 2222) 
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# Отправляем данные серверу 
s.sendto(data, sad) 
# Получаем данные порциями по 1024 байта
mfs = s.recvfrom(1024) 
# Выбираем нужную часть полученного сообщения
msg = mfs[0] 
print(msg)
```

### _Задание 2:_ Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера выполнение математической операции, параметры, которые вводятся с клавиатуры. Сервер обрабатывает полученные данные и возвращает результат клиенту. Вариант: a. Теорема Пифагора
_Для нахождения гипотенузы_
Серверная часть:
``` py
# Импортируем библиотеки socket и math
import socket
import math
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  Связываем сокет с хостом и портом
s.bind((socket.gethostname(), 2222))
# Запускаем режим прослуживания
s.listen(5)
# Принимаем подключение 
con, ad = s.accept()
msg = ''
while True:
# Получать данные будем "порциями" по 1024 байта
    data = con.recv(1024)
# Преобразовываем полученные байты в строковый объект
    msg = data.decode('utf8')
# Случай завершения сеанса
    if msg == 'over':
        print("Сеанс завершен")
        break
# Делим полученные данные по индексам
    result = 0
    cat_list = msg.split()
    cat1 = cat_list[0]
    cat2 = cat_list[1]
# Преобразовываем  строку в число
    num1 = int(cat1)
    num2 = int(cat2)
# Считаем гипотенузу
    if num1 > 0 and num2 > 0:
        result = math.sqrt(num1**2 + num2**2)
    print("Результат посчитан и отправлен")
# Преобразовываем результат в строку
    output = str(result)
# Отправляем результат, используя кодировку 
    con.send(output.encode('utf8'))
con.close()
```
Клиентская часть:
``` py
# Импортируем библиотеку socket  
import socket
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Подключаемся к другому хосту
s.connect((socket.gethostname(), 2222))
while True:
    cat = input("Введите катеты через пробел: ")
# Случай завершения сеанса 
    if cat == "over":
        break
# Отправляем строку, используя кодировку 
    s.send(cat.encode('utf8'))
# Получаем данные порциями по 1024 байта
    answer = s.recv(1024)
# Выводим результат, преобразовывая полученные байты в строковый объект
    print("Гипотенуза равна "+answer.decode('utf8'))
    print("Напишите 'over' для завершения сеанса")
s.close()
```
_Для нахождения катета_
Серверная часть:
``` py
# Импортируем библиотеки socket и math
import socket
import math
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  Связываем сокет с хостом и портом
s.bind((socket.gethostname(), 2222))
# Запускаем режим прослуживания
s.listen(5)
# Принимаем подключение 
con, ad = s.accept()
msg = ''
while True:
# Получать данные будем "порциями" по 1024 байта
    data = con.recv(1024)
# Преобразовываем полученные байты в строковый объект
    msg = data.decode('utf8')
# Случай завершения сеанса 
    if msg == 'over':
        print("Сеанс завершен")
        break
# Делим полученные данные по индексам
    result = 0
    cg_list = msg.split()
    cat1 = cg_list[0]
    gip1 = cg_list[1]
# Преобразовываем  строку в число 
    num1 = int(cat1)
    num2 = int(gip1)
# Считаем катет 
    if num1 > 0 and num2 > 0:
        result = math.sqrt(num2**2 - num1**2)
    print("Результат посчитан и отправлен")
# Преобразовываем результат в строку
    output = str(result)
# Отправляем результат, используя кодировку 
    con.send(output.encode('utf8'))
con.close()
```

Клиентская часть:
``` py
# Импортируем библиотеку socket  
import socket
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Подключаемся к другому хосту
s.connect((socket.gethostname(), 2222))
while True:
    cat = input("Введите сначала катет, а затем гипотенузу через пробел: ")
# Случай завершения сеанса 
    if cat == "over":
        break
# Отправляем строку, используя кодировку 
    s.send(cat.encode('utf8'))
# Получаем данные порциями по 1024 байта
    answer = s.recv(1024)
# Выводим результат, преобразовывая полученные байты в строковый объект
    print("Катет равен "+answer.decode('utf8'))
    print("Напишите 'over' для завершения сеанса")
s.close()
```

### _Задание 3:_ Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html.
Серверная часть:
``` py
import socket
host = 'localhost'
port = 2222
add = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((add))
s.listen(10)
while True: 
    conn, add = s.accept()
    a = "HTTP/1.0 200 OK\n"
    b = "Content-Type: text/html\n\n"
    file = open('index.html', 'r')
    cont = file.read()
    ans = a + b + cont
    conn.sendall(ans.encode("utf-8"))
    conn.close()
```
Клиентская часть:
``` py
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2222))
data = s.recv(1024)
print(data.decode('utf8'))
s.close()
```
html:
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Books shop</title>
</head>
<body>
    <center>
        <h1>Books</h1>
    </center>
    <p>We have a large selection of books!</p>
</body>
</html>
```

### _Задание 4:_ Реализовать двухпользовательский или многопользовательский чат. Реализация многопользовательского часа позволяет получить максимальное количество баллов.
Серверная часть:
``` py
# Импортируем библиотеку сокет 
import socket
import threading
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Связываем сокет с хостом и портом 
s.bind((socket.gethostname(), 2222))
# Запускаем режим прослушивания 
s.listen()
# Создаем списки 
clients = []
nicks = []
# Передача сообщений 
def broadcast(mes):
    for cli in clients:
        cli.send(mes)
def handle(cli):
    while True:
        try:
            mes = cli.recv(1024)
            broadcast(mes)
# Исключаем пользователей
        except: 
            i = clients.index(cli)
            clients.remove(i)
            broadcast(f"{nicks[i]} покинул(а) чат.".encode('utf8'))
            nicks.remove(i)
            cli.close()
            break
# Присоединение пользователей 
def recieve():
    while True:
        conn, add = s.accept()
        print(f"Подключение с адресом {add}")
        conn.send("send_nickname".encode('utf8'))
        name = conn.recv(1024)
        nicks.append(name)
        clients.append(conn)
        broadcast(f"Пользователь {name} присоединился к чату.".encode('utf8'))
        conn.send("Вы подключились".encode('utf8'))
# Многопоточность 
        part = threading.Thread(target=handle, args=(conn, ))
        part.start()
if __name__ == "__main__":
    recieve()
```

Клиентская часть:
``` py
# импортируем библиотеку сокет 
import threading
import socket
# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаемся к хосту
s.connect((socket.gethostname(), 2222))
nick = input('Для возможности переписываться необходим никнэйм. Введите его, пожалуйста: ')
# Получаем сообщения 
def to_get_mes():
    while True:
        mes = s.recv(1024)
        mesget = mes.decode('utf8')
        if mesget == "send_nickname":
            s.send(nick.encode('utf8'))
        else:
            print(mesget)
# Отправляем сообщения 
def to_send_mes():
    while True:
        messend = f"{nick}: {input('')}"
        s.send(messend.encode('utf8'))
# Создаем многопоточность 
get_part = threading.Thread(target=to_get_mes)
send_part = threading.Thread(target=to_send_mes)
# Начинаем много поточность 
get_part.start()
send_part.start()
# Блокируем поток 
# get_part.join()
send_part.join()
s.close()
```

### _Задание 5:_ Необходимо написать простой web-сервер для обработки GET и POST http запросов средствами Python и библиотеки socket.Задание: сделать сервер, который может:1 Принять и записать информацию о дисциплине и оценке по дисциплине. 2 Отдать информацию обо всех оценах по дсициплине в виде html-страницы.
Серверная часть:
``` py
import socket
import sys
MAX_LINE = 64 * 1024
class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._subjects = []
        self._marks = []
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
        data = conn.recv(16384).decode('utf8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp is not None:
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
                resp = "HTTP/1.1 200 OK\n\n"
                with open('task5_index.html', 'r') as file:
                    resp += file.read()
                return resp
            if method == 'POST':
                resp = "HTTP/1.1 204 OK\n\n"
                params = body.split('&')
                for a in params:
                    if a.split('=')[0] == 'subj':
                        self._subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        self._marks.append(a.split('=')[1])
                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, m in zip(self._subjects, self._marks):
                    resp += f"<li>Subject: {s}, Grade: {m}</li>"
                resp += "</ol></body></html>"
                return resp
    def send_response(self, conn, resp):
        conn.send(resp.encode('utf8'))
if __name__ == '__main__':
    host ='localhost'
    port = 2222
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
html:
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Journal</title>
</head>
<body>
<form action="/" method="post">
        <label for="subject">Subject:</label>
        <input type="text" name="subject" id="subject"/>
        <label for="grade">Grade:</label>
        <input type="number" name="grade" id="grade"/>
        <button>Update_journal</button>
</form>
</body>
</html>
```
