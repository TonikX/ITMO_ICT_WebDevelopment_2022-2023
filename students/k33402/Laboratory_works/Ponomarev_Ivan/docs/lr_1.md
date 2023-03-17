# Лабораторная работа 1

## Пункт 1

Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.
Обязательно использовать библиотеку socket
Реализовать с помощью протокола UDP

### Клиент

```python
import socket


host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
msg = bytes("Hello, server!\n", "utf-8")

def start_client():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.connect(serv_addr)
    connection.send(msg)
    recv_msg = connection.recv(16384)
    recv_msg_dec = recv_msg.decode("utf-8")
    print(recv_msg_dec)
    connection.close()

if __name__ == "__main__":
    start_client()

```

### Сервер

```python
import socket
import logging


host = "127.0.0.1"
port = 14900
addr = (host, port)
resp_msg = "Hello, client\n"
logging.basicConfig(filename = './log.log', filemode= 'w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

def start_server():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.bind(addr)
    logging.info("Server started")
    msg, client_addr = connection.recvfrom(16384)
    logging.info("Data received from %s port %d" % (addr[0], addr[1]))
    msg_dec = msg.decode("utf-8")
    print(msg_dec)
    connection.sendto(resp_msg.encode("utf-8"), client_addr)
    logging.info("Send response to %s" % (addr[0]))
    connection.close()        

if __name__ == "__main__":
    start_server()
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

Мой вариант: **Теорема Пифагора**

### Клиент

```python
import socket
import enum

host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class input_l(enum.Enum):

    hypotenuse = 1
    quadratic = 2
    trapezoid_area = 3
    parallelogram_area = 4
    exit = 5

class line_interface:
    def __init__(self, client):
        self.is_ex = True
        self.client = client
        self.msg = ""

    def start_li(self):
        while self.is_ex:
            self.msg=""
            print("Выберите операцию(введите цифру):\n" +
                "\n1)Теорема Пифагора" +
                "\n2)Решение квадратного уравнения" +
                "\n3)Поиск площади трапеции" + 
                "\n4)Поиск площади параллелограмма" + 
                "\n5)exit-завершение программы\n")
            act = int(input())
            if input_l.hypotenuse.value == act: self.hypotenuse()
            elif input_l.quadratic.value == act: self.quadratic()
            elif input_l.trapezoid_area.value == act: self.trapezoid_area()
            elif input_l.parallelogram_area.value == act: self.parallelogram_area()
            elif input_l.exit.value == act:
                 self.close_li()
                 break
            else: 
                print("Вы ввели неправильное число(Пример: [1] - Теорема пифагорa")
                continue
            print("iwanttosend %s"%(self.msg))
            recv_msg = self.client.send_request(self.msg)
            self.print_response(recv_msg)

    
    def quadratic(self):
        self.msg+=input_l.quadratic.name + "\n"
        print("Введите a")
        x = input()
        print("Введите b")
        b = input()
        print("Введите c")
        c = input()
        self.msg+=x + "&" + b + "&" + c


    def hypotenuse(self):
        self.msg += input_l.hypotenuse.name + "\n"
        print("Введите a")
        a = input()
        print("Введите b")
        b = input()
        self.msg+=a +"&" + b

    def trapezoid_area(self):
        self.msg += input_l.trapezoid_area.name + "\n"
        print("Введите a")
        a = input()
        print("Введите b")
        b = input()
        print("Введите h")
        h = input()
        self.msg+=a+"&"+b+"&"+h

    def parallelogram_area(self):
        self.msg+= input_l.parallelogram_area.name + "\n" 
        print("Введите a")
        a = input()
        print("Введите h")
        h=input()
        self.msg+=a+"&"+h

    def print_response(self, msg_recv):
        print(msg_recv)

    def close_li(self):
        self.client.close_connection()
        self.is_ex = False
        print("Bye!")



class client:
    def __init__(self, serv_addr, connection):
        self.serv_addr = serv_addr
        self.connection = connection
        self.start_client()

    def start_client(self):
        self.connection.connect(self.serv_addr)

    def send_request(self, msg):
        msg_b = bytes(msg, "utf-8")
        connection.send(msg_b)
        return self.rec_response()

    def rec_response(self):
        recv_msg = self.connection.recv(16384)
        recv_msg_dec = recv_msg.decode("utf-8")
        return recv_msg_dec
    
    def close_connection(self):
        self.connection.close()

if __name__ == "__main__":
    client = client(serv_addr, connection)
    line_i = line_interface(client)
    line_i.start_li()


```

### Сервер

```python
import socket
import logging
import enum
import math

host = "127.0.0.1"
port = 14900
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.basicConfig(filename = './log.log', filemode= 'w', format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

class operation(enum.Enum):
    hypotenuse = "hypotenuse"
    quadratic = "quadratic"
    trapezoid_area = "trapezoid_area"
    parallelogram_area = "parallelogram_area"

class calculation_service:
    
    def calculate(self, op, params):
        result = ""
        if op==operation.hypotenuse.value: result = self.hypotenuse(params[0],params[1])
        elif op==operation.quadratic.value: result = self.quadratic(params[0],params[1],params[2])
        elif op==operation.trapezoid_area.value: result = self.trapezoid_area(params[0], params[1], params[2])
        elif op==operation.parallelogram_area.value: result = self.parallelogram_area(params[0], params[1])
        return result

    def hypotenuse(self, a, b):
        c = (float(a)**2 + float(b)**2)**(0.5)
        return "Гипотенуза равна {}".format(c)

    def quadratic(self, a, b, c):
        a = float(a)
        b = float(b)
        c = float(c)
        discr = b ** 2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            return "x1 = {} \nx2 = {}".format(x1, x2)
        elif discr == 0:
            x = -b / (2 * a)
            return "x = {}".format(x)
        else:
            return "Корней нет"

    def trapezoid_area(self, a, b, h):
        area = ((float(a)+float(b))/2)*float(h)
        return "Площадь трапеции равна {}".format(area)

    def parallelogram_area(self, a, h):
        area = float(a) * float(h)
        return "Площадь параллелограмма равна {}".format(area)
            

class request_handler:
    def __init__(self, calculation_service):
        self.calculation_service = calculation_service

    def handle_request(self, msg_dec):
        msg_dec = msg_dec.split("\n")
        op = msg_dec[0]
        print(op)
        params = msg_dec[1].split("&")
        if self.validate(op, params):
            result = self.calculation_service.calculate(op,params)
            return result
        else:
            return "Params error"

    def validate(self, op, params):
        is_correct = False
        for oper in operation:
            if(op==oper.value): is_correct = True
        for param in params:
            try:
                int(param)
            except ValueError as ve:
                return False  
        return is_correct  

class server:
    def __init__(self, connection, req_handler, addr):
        self.connection = connection
        self.request_handler = req_handler
        self.addr = addr
        self.start_server()

    def start_server(self):
        self.connection.bind(addr)
        self.connection.listen(10)
        logging.info("Server started")
        client_socket, client_addr = self.connection.accept()
        self.get_request(client_socket, client_addr)

    def send_response(self, resp_msg, client_socket):
        client_socket.send(resp_msg)
        logging.info("Send response to %s" % (addr[0]))

    def get_request(self, client_sock, addr):
        while True:
            try:
                msg = client_sock.recv(16384)
                logging.info("Data received from %s port %d" % (addr[0], addr[1]))
                msg_dec = msg.decode("utf-8")
                response = self.request_handler.handle_request(msg_dec)
                response_encoded = response.encode("utf-8")
                self.send_response(response_encoded, client_sock)
            except:
                client_sock.close()
                break

if __name__ == "__main__":
    request_handler = request_handler(calculation_service())
    server = server(connection, request_handler, addr)

```

## Пункт 3

Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

### Клиент
```python
import socket


host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class client:
    def __init__(self,connection, serv_addr):
        self.connection = connection
        self.start_client(serv_addr)

    def start_client(self, serv_addr):
        self.connection.connect(serv_addr)
        self.get_response()

    def get_response(self):
        while True:
            recv_data = self.connection.recv(1024)
            if not recv_data:
                break
            print(recv_data.decode("utf-8"))

if __name__=="__main__":
    client = client(connection, serv_addr)
```

### Сервер

```python
import socket
import codecs

host = "127.0.0.1"
port = 14900
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class reader:
    def __init__(self, path):
        self.path = path
    def read_html(self):
        file = codecs.open(self.path, "r", "utf_8_sig" )
        text = file.read()
        file.close()
        return text

class server:
    def __init__(self, connection, serv_addr, reader):
        self.connection = connection
        self.reader = reader
        self.serv_addr = serv_addr
        self.start_server()
  
    def start_server(self):
        self.connection.bind(self.serv_addr)
        self.connection.listen(10)
        clientsocket, client_addr = self.connection.accept()
        self.send_resp(clientsocket)
    
    def send_resp(self, client_socket):
        response = self.build_resp()
        client_socket.send(response)
        print('{} senderd' %(response))
        client_socket.close()

    def build_resp(self):
        type = 'HTTP/1.0 200 OK\r\n'
        headers = 'Content-Type: text/html\r\n\r\n'
        body = self.reader.read_html()
        response = type + headers + body
        response_enc = response.encode("utf-8")
        return response_enc




if __name__=="__main__":
    reader = reader('index.html')
    server = server(connection, addr, reader)        
```
## HTML страница
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <title>weblab/</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <link rel="stylesheet" type="text/css" href="css/style.css">
</head>
<body>
<table class="generalTable" border="1">
    <tr>
        <td style="padding-bottom:3%" colspan="3">
            <header>
                <center>
                    <h1>Пономарев И.C</h1>
                    <b>Вариант:</b> 12027
                    <b>Группа:</b> P3212
                </center>
            </header>
        </td>
    </tr>
    <tr>
        <td width="1%">
            <img src="img/img.PNG">
        </td>
        <td width="18%">
            <div id="radioCoordinate">
                <b>Выберите параметр R</b>:
                <p><input type="radio" name="paramR" value="1" checked>1</p>
                <p><input type="radio" name="paramR" value="1.5">1,5</p>
                <p><input type="radio" name="paramR" value="2">2</p>
                <p><input type="radio" name="paramR" value="2.5">2,5</p>
                <p><input type="radio" name="paramR" value="3">3</p>
            </div>
            <div id="checkBoxCoordinates">
                <b>Выберите координату X</b>:
                <p><input type="checkbox" name="coordX" value="-3" checked>-3
                    <input type="checkbox" name="coordX" value="-2" >-2
                    <input type="checkbox" name="coordX" value="-1" >-1</p>
                <p></p><input type="checkbox" name="coordX" value="0" > 0
                <input type="checkbox" name="coordX" value="1" > 1
                <input type="checkbox" name="coordX" value="2" > 2</p>
                <p><input type="checkbox" name="coordX" value="3" > 3
                    <input type="checkbox" name="coordX" value="4" > 4
                    <input type="checkbox" name="coordX" value="5" > 5</p>
            </div>
            <div id="inputCoordinate">
                <b>Введите координату Y</b>:
                <input size=11% type="text" class="number" name="coordY" required>
                <input type="submit" class="button" id="send" value="Send">
            </div>
        </td>
        <td style="padding-left:5%"><div id="outputContainer" class="OUT"></div></td>
    </tr>
    <tr>
        <td style="padding-top:2%" colspan="3"><center><iframe src="https://wayou.github.io/t-rex-runner/" frameborder="0" scrolling="no" width="100%" height="100%"></iframe></center></td>
    </tr>
</table>
<script src="js/main.js"></script>
</body>
</html>
```



## Пункт 4

Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

### Клиент

```python
import socket
import threading

host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exit_event = threading.Event()

def start_client():
    is_conn = True
    connection.connect(serv_addr)
    connection.send(input("Enter your name: ").encode("utf-8"))
    thread = threading.Thread(target=get_message)
    thread.start()
    while is_conn:
        message = input("")
        print("\033[A",end="")
        for i in range(0,len(message)):
            print(" ", end = "")
        print("\r",end="")
        if message == 'bye':
            exit_event.set()
            is_conn = False
        connection.send(message.encode("utf-8"))
    connection.close()

def get_message():
    while True:
        if exit_event.is_set():
            break
        try:
            message = connection.recv(16384)
            message_dec = message.decode('utf-8')
            print(message_dec)
        except:
            break
   
if __name__ == "__main__":
    start_client()
```

### Сервер

```python
import socket
import logging
import threading

host = "127.0.0.1"
port = 14900
addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class server:
    def __init__(self, connection, serv_addr):
        self.connection = connection
        self.serv_addr = serv_addr
        self.clients = dict()
        self.start_server()
    
    def start_server(self):
        self.connection.bind(self.serv_addr)
        self.connection.listen(10)
        while True:
            client, client_addr = self.connection.accept()
            name=client.recv(16384)
            self.clients[client]=name.decode("utf-8")
            thread = threading.Thread(target=self.handle_message, args = (client,))
            thread.start()
            
    def handle_message(self,client):
        while True:
            message = client.recv(16384)
            message_e = message.decode('utf-8')
            if message_e == 'bye':
                self.clients.pop(client)
                client.close()
                break
            self.send_message(message_e, self.clients[client])

    def send_message(self,message,user_message):
        for client in self.clients.keys():
                client.send(("%s: %s"%(user_message,message)).encode("utf-8"))




if __name__ == "__main__":
    server = server(connection, addr)
```

## Пункт 5

Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:
● Принять и записать информацию о дисциплине и оценке по дисциплине.
● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

### Клиент

```python
import socket 

host = '127.0.0.1'
port = 14901
addr = (host,port)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(addr)
subject = input("Enter a subject: ")
mark = input("Enter a mark: ")
message = f'POST /marks?subject={subject}&mark={mark} HTTP/1.1\r\n'
message += 'Host: example.com\r\n'
message += 'Accept: text/html\r\n\r\n'
message_enc = message.encode("utf-8")
socket.send(message_enc)
recv = socket.recv(16384)
recv_decode = recv.decode("utf-8")
print(recv_decode)
```

### Сервер

```python
import socket
import sys
import request,response
import marks_dao
import HTTPError

class MyHTTPServer:
    def __init__(self, host, port, name, marks_dao):
        self.host = host
        self.port = port
        self.name = name
        self.marks_dao = marks_dao

    def serve_forever(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind((self.host, self.port))
        connection.listen()
        while True:
            client, addr = connection.accept()
            self.serve_client(client)

    def serve_client(self, client):
        try:
            req = self.parse_request(client)
            response = self.handle_request(req)
            self.send_response(response, client)
        except HTTPError as err:
            self.send_error(client, err)

    def parse_request(self, client):
        rfile = client.makefile("rb")
        line = rfile.readline()
        line = line.decode("utf-8")
        line = line.rsplit("\r\n")
        words = line[0].split()
        method, target, ver = words
        headers = self.parse_headers(rfile)
        if headers["Host"] not in (self.name, f'{self.host}:{self.port}'):
            raise HTTPError(404, 'not found')
        return request.request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = dict()
        while True:
            line = rfile.readline()
            if b'\r\n'== line:
                print("found end of headers")
                break
            line = line.decode("utf-8")
            line = line.rsplit("\r\n")
            words = line[0].split(": ")
            header, value = words
            headers[header]=value
        return headers

    def handle_request(self, request):
        if  request.method == "GET" and request.path=="/marks" and request.query:
            return self.handle_get_certain_marks(request)
        elif request.method == "POST" and request.path=="/marks":
            return self.handle_post_marks(request)
        elif  request.method == "GET" and request.path=="/marks":
            return self.handle_get_marks(request)
        else: raise Exception("not found")
    
    def handle_get_certain_marks(self, request):
        path_variable = request.query
        subject = path_variable['subject'][0]
        body = self.body_builder(request, subject)
        content_type, body = body
        headers = {'Content-Type': content_type, 'Content-Length': len(body)}
        return response.response(200, "OK", headers, body)

    def handle_get_marks(self, request):
        body = self.body_builder(request)
        content_type, body = body
        headers = {'Content-Type': content_type, 'Content-Length': len(body)}
        return response.response(200, "OK", headers, body)

    def body_builder(self,request, subject=None):
        accept = request.headers['Accept']
        if 'text/html' in accept:
            content_type = "text/html; charset=utf-8"
            body = '<!DOCTYPE html>'
            body += '<html lang="en"><head><title>lol</title>'
            body+= '<link rel="icon" href="data:;base64,=">'
            body += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
            body += '</head><body>'
            body += '<div>Оценки</div>'
            body +='<ul>'
            if not subject:
                marks = self.marks_dao.get_marks()
                for key in marks:
                    body+=f'<li>{key}: '
                    for mark in marks[key]:
                        body+=f'{str(mark)} '
                    body+='</li>'
            else: 
                marks = self.marks_dao.get_marks_subject(subject)
                print(marks)
                body+=f'<li>{subject}: '
                for mark in marks:
                    body+=f'{str(mark)} '
                body+='</li>'
            body+='</ul>'
            body+='</body></html>'
        return (content_type, body)

    def handle_post_marks(self, request):
        path_variables = request.query
        self.marks_dao.add(path_variables["subject"][0], path_variables["mark"][0])
        return response.response(204, "Created")

    def send_response(self, response, connection):
        wfile = connection.makefile('wb')
        status = f'HTTP/1.1 {response.status} {response.reason}\r\n'
        wfile.write(status.encode("utf-8"))
        print(status)
        if response.headers:
            for key in response.headers.keys():
                header = f'{key}: {response.headers[key]}\r\n'
                wfile.write(header.encode("utf-8"))
        print(response.headers)
        wfile.write(b'\r\n')

        if response.body:
            wfile.write(response.body.encode("utf-8"))
        print(response.body)
        wfile.flush()
        wfile.close()
    
    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
            resp = response(status, reason,
                   [('Content-Length', len(body))],
                   body)
        self.send_response(conn, resp)
        
if __name__ == '__main__':
  host = '127.0.0.1' 
  port = 14901
  name = 'example.com'
  marks_dao = marks_dao.marks_dao("marks.txt")
  serv = MyHTTPServer(host, port, name, marks_dao)
  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass
```
### HTTP ERROR

```python
class HTTPError(Exception):
  def __init__(self, status, reason, body=None):
    super()
    self.status = status
    self.reason = reason
    self.body = body
```

### marks_dao

```python
class marks_dao:
    def __init__(self, path_to_data):
        self.path_to_data = path_to_data
        self.marks = dict()
        self.fill_dict()

    def fill_dict(self):
        file = open(self.path_to_data,"r")
        text = file.read().split("\n")
        if "" in text: text.remove("")
        if len(text) == 0:
            print("Src file is empty. No info about marks")
            return
        for line in text:
            row = list()
            line = line.split(": ")
            subject, marks = line
            marks = marks.split()
            if "" in marks: marks.remove("")
            for mark in marks:
                row.append(int(mark))
            self.marks[subject] = row
        print("Dictionary filled")
        file.close()

    def add(self, subject, mark):
        if subject not in self.marks.keys():
            self.marks[subject] = list()
        self.marks[subject].append(int(mark))
        self.update_file()

    def update_file(self):
        file = open(self.path_to_data, "w")
        for key in self.marks:
            file.write("%s: "%(key))
            for mark in self.marks[key]:
                file.write("%d "%(mark))
            file.write("\n")
        file.flush()
        file.close()
    
    def get_marks(self):
        return self.marks
    
    def get_marks_subject(self, subject):
        if subject not in self.marks.keys():
            raise Exception("not found")
        return self.marks[subject]
```

### request.py

```python
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

class request:
    def __init__(self, method, target, version, headers, rfile):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile

    @property
    def path(self):
        return self.url.path
    
    @property
    def query(self):
        return parse_qs(self.url.query)
    
    @property
    def url(self):
        return urlparse(self.target)
        
```

### response.py
```python
class response:
    def __init__(self, status, reason, headers = None, body = None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```
