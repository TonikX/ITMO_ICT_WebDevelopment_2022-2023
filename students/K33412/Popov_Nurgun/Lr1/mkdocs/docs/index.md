# ЛАБОРАТОРНАЯ РАБОТА 1

## TASK 1
* client.py
``` py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5678))
client_socket.sendall('Hello, server'.encode())
data = client_socket.recv(1024).decode()
print(data)
```
* server.py
``` py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5678))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()
    data = client_socket.recv(1024).decode('ascii')
    print(data)
    client_socket.send('Hello, client'.encode())

```
## TASK 2
* client.py
``` py 
import socket

#Version with trapezoid

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5678))
msg = client_socket.recv(1024).decode()
print(msg)
parameters_str = input()
client_socket.sendall(parameters_str.encode())
data = client_socket.recv(1024).decode()
print(data)

```
* server.py
``` py
import socket

#Version with trapezoid
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5678))

server_socket.listen(5)

def calculate_area_of_trapezoid(base1, base2, height):
    return (base1 + base2) / 2 * height

while True:
    client_socket, address = server_socket.accept()
    client_socket.send('Enter parameters of trapezoid separated by space: base1 base2 height'.encode())
    data = client_socket.recv(1024).decode('ascii').split(' ')
    result = calculate_area_of_trapezoid(int(data[0]), int(data[1]), int(data[2]))
    client_socket.send(str(result).encode())
```
## TASK 3
* client.py
``` py
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5678))
data = client_socket.recv(1024).decode()
print(data)
```
* server.py
``` py
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5678))

server_file = open('server_index.html', 'wb')

server_socket.listen(5)

client_socket, address = server_socket.accept()
server_file = open('index.html', 'rb')

client_socket.sendfile(server_file)
```
* index.html
``` html
<!DOCTYPE html>

<html>
    <head>
        Лабораторная работа №1
    </head>
    <body>
        <b>Часть 3</b>
    </body>
</html>
```
## TASK 4
* client.py
``` py
import socket
import threading

class Client():
    def __init__(self):
        self.username = input('Enter your username: ')
        self.sock = socket.socket()
        self.sock.connect(('localhost', 5678))
        self.sock.sendall((self.username + ' endered chat').encode())
        print('You entered chat as ' + self.username)

    def send_messages(self):
        try:
            while True:
                msg = input()
                if msg == '\\quit':
                    print('You exited chat')
                    self.sock.sendall((self.username + ' exited chat').encode())
                    break
                self.sock.sendall((self.username + ': ' + msg).encode())
        except Exception:
            pass

    def check_messages(self):
        try:
            while True:
                new_msg = self.sock.recv(1024).decode()
                if new_msg:
                    print(new_msg)
        except Exception:
            pass

if __name__=='__main__':
    client = Client()
    threading.Thread(target=client.check_messages, args=()).start()
    threading.Thread(target=client.send_messages, args=()).start()

```
* server.py
``` py
import socket
import threading

class Server():
    def __init__(self):
        self.user_list = []
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('localhost', 5678))
        self.sock.listen(5)
        print('Server started')

    def run(self):
        try:
            while True:
                client_sock, addr = self.sock.accept()
                self.user_list.append(client_sock)
                threading.Thread(target=self.check_messages, args=(client_sock,)).start()
        except KeyboardInterrupt:
            self.user_list = []
            self.sock.close()

    def check_messages(self, client_sock):
        try:
            while True:
                msg = client_sock.recv(1024).decode('utf-8')
                if msg:
                    self.show_msg(client_sock, msg)
        except Exception:
            self.terminate_connection(client_sock)

    def terminate_connection(self, client_sock):
        self.user_list.remove(client_sock)

    def show_msg(self, client_sock, msg):
        print(msg)
        for user in self.user_list:
            if user != client_sock:
                user.sendall(msg.encode())

if __name__=='__main__':
    server = Server()
    main_thread = server.run()

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


# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
