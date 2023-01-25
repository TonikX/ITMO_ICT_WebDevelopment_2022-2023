# ЛАБОРАТОРНАЯ РАБОТА 1
## TASK 1
* client.py
``` py
import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.send(b"Hello, server! \n")

data = sock.recv(16384)
print(data.decode("utf-8"))
sock.close()
```
* server.py
``` py
import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

clientsocket, address = sock.accept()
data = clientsocket.recv(16384)
udata = data.decode("utf-8")
print(udata)
clientsocket.send(b"Hello, client! \n")
sock.close()
```
## TASK 2
* client.py
``` py 
import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

   #Version with trapezoid

for i in range(3):
    data = sock.recv(16384)
    text = data.decode()
    print(text)
    proportions = input()
    sock.send(proportions.encode())

data = sock.recv(16384)
trapezoid_area = data.decode()
print(trapezoid_area)
sock.close()
```
* server.py
``` py
import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(10)

#Version with trapezoid

clientsocket, address = sock.accept()
clientsocket.send(b"Enter large trapezoid base:")
data = clientsocket.recv(16384)
large_base = int(data.decode())
clientsocket.send(b"Enter small trapezoid base:")
data = clientsocket.recv(16384)
small_base = int(data.decode())
clientsocket.send(b"Enter trapezoid height:")
data = clientsocket.recv(16384)
height = int(data.decode())
area = height * ((large_base + small_base) / 2)
clientsocket.send(f"Trapezoid area: {area}".encode())
sock.close()
```
## TASK 3
* client.py
``` py
import socket

conn = socket.socket()

conn.connect(("127.0.0.1", 7779))
result = conn.recv(10000)
print(result.decode())
conn.close()
```
* server.py
``` py
import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 7779
server.bind((host, port))
server.listen(1)

while True:
    conn, addr = server.accept()

    page = open('index.html')
    content = page.read()
    page.close()

    response = 'HTTP/1.0 200 OK\n\n' + content
    conn.sendall(response.encode())
    conn.close()
```
* index.html
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>A tiny tiny page</title>
</head>
<body>
    <p>
        "We want a few mad people now. See where the sane ones have landed us!"
    </p>
    <p>
         George Bernard Shaw (1856-1950)
    </p>
</body>
</html>
```
## TASK 4
* client.py
``` py
import socket
import threading


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = '127.0.0.1', 8080
conn.connect(server)

username = input('Выберите псевдоним: ')


def recv_msg():
    while True:
        msg = conn.recv(2000).decode()
        if msg == 'username':
            conn.send(username.encode())
        else:
            print(msg)


def print_msg():
    while True:
        msg = '{} says: {}'.format(username, input(''))
        conn.send(msg.encode())


recv_thr = threading.Thread(target=recv_msg)
print_thr = threading.Thread(target=print_msg)
recv_thr.start()
print_thr.start()
```
* server.py
``` py
import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
server.bind((host, port))
server.listen()

clients = []
users = []


def broadcast(msg, client):
    for each in clients:
        if each != client:
            each.send(msg)


def handle(client):
    while True:
        msg = client.recv(2000)
        broadcast(msg, client)


def receive():
    while True:
        client, addr = server.accept()
        client.send('username'.encode())
        user = client.recv(2000).decode()
        clients.append(client)
        users.append(user)
        client.send('Connection established'.encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
```
## TASK 5
* server.py
``` py
import socket

class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(2)
        while True:
            clientsocket, _ = sock.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(18456)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, target, protocol = lines[0].split()
        return target, method

    def parse_headers(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        i = lines.index('')
        headers = lines[1:i]
        body = lines[-1]
        return headers, body

    def handle_request(self, target, method, body):
        if target == "/":
            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

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

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))

if __name__ == '__main__':
    host = 'localhost'
    port = 8081
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
* index.html
``` html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Journal</title>
</head>
<body>
<form action="/" method="post">
    <div>
        <label for="name">Subject:</label>
        <input type="text" id="name" name="subject"/>
    </div>
    <div>
        <label for="mail">Mark:</label>
        <input type="number" id="mail" name="mark"/>
    </div>
    <div>
        <input type="submit">
    </div>

</body>
</html>
```

