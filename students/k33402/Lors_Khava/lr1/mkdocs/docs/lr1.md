# Laboratory work 1
---

- server.py - серверная часть
- client.py - клиентская часть 

---
## Task 1

* server.py
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(1)

clientsocket, address = server.accept()
data = clientsocket.recv(1024)
print(data.decode("utf-8"))
clientsocket.send("Hello, client!".encode("utf-8"))
clientsocket.close()
```

* client.py
```pytnon
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080))

client.send("Hello, server!".encode("utf-8"))
data = client.recv(1024)
print(data.decode("utf-8"))
client.close()
```
---
## Task 2

* server.py 

```python 
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080)) 
server.listen(10) 

while True:
    try:
        clientsocket, address = server.accept()
        data = clientsocket.recv(1024).decode("utf-8") 
        a, b, c = float(a), float(b), float(c)
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            msg = "No solutions"
            clientsocket.send(msg.encode("utf-8")) 
        elif d == 0:
            x = -b / (2*a)
            clientsocket.send(f"x = {x}".encode("utf-8")) 
        else:
            x1 = (-b-d ** 0.5)/(2*a)
            x2 = (-b+d ** 0.5)/(2*a)
            clientsocket.send(f"x1 = {x1}, x2 = {x2}".encode("utf-8")) 

    except KeyboardInterrupt: 
        server.close() 
        break
```
* client.py

```python 
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080)) 

num = input("Enter a, b, c: \n") 
client.send(num.encode("utf-8")) 
data = client.recv(1024).decode("utf-8") 
print("result: ", data) 
client.close()
```
---
## Task 3

* index.html

```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
</head>
<body>
    <p>
        "Today is a beautiful day!"
    </p>
</body>
</html>
```

* server.py

```python 

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(10)

while True:
    try:
        clientsocket, address = server.accept()
        html_p = open('index.html')
        html_content = html_p.read()
        html_p.close()

        html_resp = 'HTTP/1.0 200 OK\n' + html_content 

        clientsocket.sendall(html_resp.encode('utf-8'))
        clientsocket.close()
        
    except KeyboardInterrupt: 
        server.close() 
        break
```
* client.py 

```python 
from http import client
import socket 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 8080))
data = client.recv(1024)
print(data.decode('utf-8'))
client.close()
```
---
## Task 4

* server.py 

```python 
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(10)

clients = []
nicknames = []

def broadcast(message):
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
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()
```

* client.py

```python
import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080)) 


def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
```
---
## Task 5

* server.py 

```python 
import socket

GRADES = {}


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(10)
        while True:
            cliensocket, address = server.accept()
            self.serve_client(cliensocket)

    def serve_client(self, clientsocket):
        try:
            req = self.parse_request(clientsocket)
            resp = self.handle_request(req)
            self.send_response(clientsocket, resp)
        except ConnectionResetError:
            clientsocket = None
        if clientsocket:
            clientsocket.close()


    def parse_request_line(self, rfile):
        line = rfile.readline(10**4)
        line = line.decode("utf-8")
        return line.split()

    def parse_request(self, clientsocket):
        rfile = clientsocket.makefile('rb')
        method, url, ver = self.parse_request_line(rfile)
        request = {'data': {}, 'method': method}
        if '?' in url:
            request['method'] = 'POST'
            values = url.split('?')[1].split('&')
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
        contenttype = 'text/html; charset=utf-8'
        body = '<html><head><style></style></head><body>'
        body += '<form><label>Discipline </label><input name="discipline" /><br><label>Mark </label><input name="grade"/><br><input type="submit"></form>'
        for i in GRADES:
            body += f'<div><span>{i}: {GRADES[i]}</span></div>'
        body += '</div></body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', contenttype),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in GRADES:
            GRADES[discipline] = []

        GRADES[discipline].append(grade)

        return self.handle_get()

    def send_response(self, clientsocket, resp):
        rfile = clientsocket.makefile('wb')
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
    serv = MyHTTPServer('127.0.0.1', 8080)
    serv.serve_forever()
```











