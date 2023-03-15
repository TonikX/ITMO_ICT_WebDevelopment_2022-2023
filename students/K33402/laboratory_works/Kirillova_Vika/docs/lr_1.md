# Лабораторная работа №1

## Задача №1

* `server.py`
 
```python
import socket

conn = socket.socket()
conn.bind (("127.0.0.1", 3300))
conn.listen(1)

clientsocket, address = conn.accept()
data = clientsocket.recv(1024)
print(data.decode("utf-8"))

clientsocket.send("Hello, client".encode("utf-8"))

clientsocket.close()
```

* `client.py`

```python
import socket

client = socket.socket()
client.connect (("127.0.0.1", 3300))

client.send("Hello, server".encode("utf-8"))

data = client.recv(1024)
print(data.decode("utf-8"))
```

## Задача №2

* `server.py`

```python
import socket
import math
import pickle

conn = socket.socket()
conn.bind (("127.0.0.1", 3300))
conn.listen(1)

while True:
	try: 
		clientsocket, address = conn.accept()
		datz = clientsocket.recv(1024)
		numb = pickle.loads(datz)
		a = int(numb.get('a'))
		b = int(numb.get('b'))
		c = int(numb.get('c'))
		discr = b ** 2 - 4 * a * c
		if discr > 0: 
			x1 = (- b + math.sqrt(discr)) / (2 * a)
			x2 = (- b - math.sqrt(discr)) / (2 * a)
			clientsocket.send(b"x1 = " + (str(x1).encode("utf-8")) + b" x2 = " + (str(x2).encode("utf-8")))
		elif discr == 0:
			x = - b / (2 * a)
			clientsocket.send(b"x = " + (str(x).encode("utf-8")))
		else:
			clientsocket.send("Корней нет".encode("utf-8"))
	except KeyboardInterrupt:
		conn.close()
		break

 conn.close()
```

* `client.py`

```python
import socket
import pickle

client = socket.socket()
client.connect(("127.0.0.1", 3300)) 

numb = {
	"a": input("Введите значение а: "),
	"b": input("Введите значение b: "),
	"c": input("Введите значение c: ")
}
numb=pickle.dumps(numb)
client.send(numb) 

data = client.recv(1024)
print(data.decode("utf-8"))

client.close()
```

## Задача №3

* `server.py`

```python
import socket

conn = socket.socket()
conn.bind(("127.0.0.1", 3300))
conn.listen(1)

while True:
    try:
        clientsocket, address = server.accept()
        html_page = open('index.html')
        html_content = html_page.read()
        html_page.close()

        html_resp = 'HTTP/1.0 200 OK\n' + html_content 

        clientsocket.send(html_resp.encode('utf-8'))
        clientsocket.close()

    except KeyboardInterrupt: 
        conn.close() 
        break
```

* `client.py`

```python
from http import client
import socket 

client = socket.socket()
client.connect(("127.0.0.1", 3300))

data = client.recv(1024)
print(data.decode('utf-8'))

client.close()
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Home page</title>
</head>
<body>
    <p>
        "Hello!"
    </p>
</body>
</html>
```

## Задача №4

* `server.py`

```python
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1', 3300))
server.listen(100)

clients = list()
end = list()

def accept():
 
    while True:
        client, addr = server.accept()
        clients.append(client)
        print (f'Текущее количество подключений: {client}')
 
 
def recv_data(client):
    while True:
        try:
            indata = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            break
        print(indata.decode('utf-8'))
        for clien in clients:
            if clien != client:
                clien.send(indata)
 
 
def outdatas():
    while True:
        print('')
        outdata = input('')
        print()
        if outdata=='enter':
            break
        for client in clients:
            client.send (f"Сервер: {outdata}". encode ('utf-8)'))
 
 
def indatas():
    while True:
            for clien in clients:
                if clien in end:
                    continue
                index = threading.Thread(target = recv_data,args = (clien,))
                index.start()
                end.append(clien)
 

t1 = threading.Thread(target = indatas,name = 'input')
t1.start()
 
t2 = threading.Thread(target = outdatas, name= 'out')
t2.start()
 
t3 = threading.Thread(target = accept(),name = 'accept')
t3.start()

t2.join()

for client in clients:
    client.close()
```

* `client.py`

```python
import socket
import threading
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    name = input("Как вас зовут?")
    if 1<len(name)<10:
        break

client.connect(('127.0.0.1', 3300))
 
 
def outdatas():
    while True:
        outdata = input('')
        if outdata=='enter':
            break
        client.send(f'{name}:{outdata}'.encode('utf-8'))
        print('%s:%s'% (name, outdata))
 
 
def indatas():
    while True:
        indata = client.recv(1024)
        print(indata.decode('utf-8'))

t1 = threading.Thread(target=indatas, name='input')

t2 = threading.Thread(target=outdatas, name='out')

t1.start()
t2.start()

t2.join()
 
client.close()
```

## Задача №5

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
        body = '<html><head><style>body {background-color:pink}</style></head><body>'
        body += '<form>Предмет<br><input name="discipline" /><br><br>Оценки<br><input name="grade"/><br><br><input type="submit"></form> <table> <tr> <th>Дисциплина</th> <th>Оценки</th> </tr> '
 
        for subject in grades:
            body += f'<tr> <th>{subject}</th> <th> {grades[subject]}</th> </tr>'
        body += '</body></html>'
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
    serv = MyHTTPServer('127.0.0.1', 1025)
    serv.serve_forever()
```