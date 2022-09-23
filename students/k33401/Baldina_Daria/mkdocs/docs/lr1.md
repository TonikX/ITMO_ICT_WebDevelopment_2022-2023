# Лабораторная работа №1

## Задача №1

* `server.py`
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8080)) 
s.listen(1)
conn, addr = s.accept() 

while True:
	data = conn.recv(1024) #получаем данные из сокета.
	if not data:
		break
	conn.sendall('Hello, client.'.encode('utf-8')) 
	print(data.decode('utf-8'))
conn.close()
```

* `client.py`
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8080))
s.sendall('Hello, server.'.encode('utf-8')) # отправляем фразу.
data = s.recv(1024) #получаем сообщение из сокета.
print(data.decode('utf-8'))
s.close()
```

## Задача №2
* `server.py`
```python
from math import sqrt

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    list_of_coef = data.decode('utf-8').split(',')
    for i in range(len(list_of_coef)):
        list_of_coef[i] = int(list_of_coef[i])
    #математические подсчеты
    d = list_of_coef[1]**2 - 4*list_of_coef[0]*list_of_coef[2]
    if d < 0:
        conn.sendall('Нет  решений'.encode('utf-8'))
    elif d == 0:
        result = 'Корень уравнения: ' + str(round(-list_of_coef[1]/(2*list_of_coef[0]),3))
        conn.sendall(result.encode('utf-8'))
    else:
        result = 'Корни квадратного уравнения: ' + str(round((-list_of_coef[1]-sqrt(d))/(2*list_of_coef[0]),3)) + ' ' + str(round((-list_of_coef[1]+sqrt(d))/(2*list_of_coef[0]),3))
        conn.sendall(result.encode('utf-8'))
conn.close()
```

* `client.py`
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
print('Введите коэффициенты квадратного уравнения')
a, b, c = map(int, input().split())
s.sendall((str(a)+','+str(b)+','+str(c)).encode('utf-8'))
answer = s.recv(1024)
print(answer.decode('utf-8'))
s.close()
```

## Задача №3
* `server.py`
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 555))
s.listen(1)

while True:
    conn, addr = s.accept()
    #работа с файлом
    html_page = open('index.html')
    html_content = html_page.read()
    html_page.close()

    html_response = 'HTTP/1.0 200 OK\n' + html_content 

    conn.sendall(html_response.encode('utf-8'))
    conn.close()
```

* `client.py`
```python
import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 555))
data = s.recv(1024) #получаем сообщение из сокета.
print(data.decode('utf-8'))
s.close()
```

* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test page</title>
</head>
<body>
    <p>
        "Hello, world!"
    </p>
</body>
</html>
```

## Задача №4
* `server.py`
```python
import threading, socket


def send_to_chat(sender, msg):
    for client in clients:
        if sender != client:
            client.sendall(msg)

def handle_client(cl_sock, cl_addr): #обработка клиента
    print(f'Client {cl_addr[0]}:{cl_addr[1]} join the chat')

    while True:
        try:
            message = cl_sock.recv(1024) #принимаем сообщение от клиента
            if message.decode('utf-8').find('bye') != -1: #клиент покидает 
                send_to_chat(cl_sock, message) 
                break
            elif message.decode('utf-8').find('Error') != -1:
                break
            send_to_chat(cl_sock, message)  #отправляем сообщение участникам чата
        except socket.error:
            print(f'Client {cl_addr[0]}:{cl_addr[1]} suddenly left')
            break

    print (f'Client {cl_addr[0]}:{cl_addr[1]} left the chat')
    clients.remove(cl_sock)
    cl_sock.close()

#запускаем сервер
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
s.bind((host,port))
s.listen(100)
clients = []

print('Starting chat server')


while True:
        try:
            client_socket, client_address = s.accept()
            if client_address not in clients:
                clients.append(client_socket)
            t1 = threading.Thread(target = handle_client, args =(client_socket, client_address))
            t1.start()
        except KeyboardInterrupt:
            print('Server stopped')
            break
s.close()
```

* `client.py`
```python
import socket, threading, time

shutdown = False

def recive():
    while not shutdown:
        try:
            data = s.recv(1024).decode('utf-8')
            print(data)
        except socket.error:
            time.sleep(0.5)
            continue


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
s.connect((host,port))
s.setblocking(0)

alias = input("Name: ")
print('If you want to leave the chat write: bye')
rt = threading.Thread(target = recive)
rt.start()


while True:
    try:
        message = input()
        s.sendall((f'{alias} :: {message}').encode('utf-8'))
        if message == 'bye':
            print('You left the chat')
            shutdown = True
            break
    except:
        s.sendall('Error'.encode('utf-8'))
        print('Error. Disconected')
        shutdown = True
        break
s.close()
```

## Задача №5

* `http_server_task_5.py`
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
        serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self.host, self.port))
            serv_sock.listen()
            while True:
                client, address = serv_sock.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            serv_sock.close()

    
    def serve_client(self, client):
        try:
            data = client.recv(1024).decode('utf-8')
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        except Exception as e:
                print(e)
        client.close()

    def parse_request(self, data):
        req = data.rstrip('\r\n')
        words = req[:data.index("\n")].split()
        if len(words) != 3:                 
            raise Exception('Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

    
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
        body += '<form><label>Дисциплина</label><input name="discipline" /><br><label>Оценка</label><input name="grade"/><input type="submit"></form>'
        for subject in self.marks:
            body += f'<div><span>{subject}: {self.marks[subject]}</span></div>'
        body += '</div></body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in self.marks:
            self.marks[discipline] = []

        self.marks[discipline].append(grade)

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

    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.


if __name__ == '__main__':
  host = '127.0.0.1' 
  port = 8000
  serv = MyHTTPServer(host, port)
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass
```