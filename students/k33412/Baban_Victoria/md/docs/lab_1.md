# Лабораторная работа 1. Работа с сокетами

## Задание 1

* server.py


```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
conn, addr = sock.accept()

print('connected with:', addr)

while True:
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    conn.send(b'Hello, client.\n')

conn.close()
```


* client.py


```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9523))
sock.send(b'Hello, server.\n')

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()
```
## Задание 2

**Вариант:** Теорема Пифагора

* server.py

```
import socket
from math import sqrt

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024).decode()
    try:
        data = data.split(" ")
        katet_1 = float(data[0])
        katet_2 = float(data[1])
        gipotenyza = float(data[2])
    except:
        conn.sendall('Неверный формат входных данных!\n'.encode())
    else:
        if katet_2 == 0:
            katet_2 = sqrt(gipotenyza**2 - katet_1**2)
            conn.sendall(f'Второй катет имеет длину: {katet_2}\n'.encode())
        elif gipotenyza == 0:
            gipotenyza = sqrt(katet_1**2 + katet_2**2)
            conn.sendall(f'Гипотенуза имеет длину: {gipotenyza}\n'.encode())
        else:
            if gipotenyza == sqrt(katet_1**2 + katet_2**2):
                conn.sendall('Теорема Пифагора выполняется. Всё верно, это - прямоугольный треугольник.'.encode())
            else:
                conn.sendall('Теорема Пифагора не выполняется. Треугольник не прямоугольный!'.encode())

    if not data:
        break
    conn.send(b'Hello, client.\n')

conn.close()
```

* client.py

```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9523))

data = input("Введите значение одного из катетов: ").replace(" ", "")
data += " " + input("Введите значение второго катета, если оно известно, иначе - введите 0: ").replace(" ", "")
data += " " + input("Введите значение гипотенузы, если оно известно, иначе - введите 0: ").replace(" ", "")
sock.send(data.encode())


result = sock.recv(1024)
print(result.decode("utf-8"))

sock.close()
```

## Задание 3

* server.py

```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
conn, addr = sock.accept()
print('connected with:', addr)

with open('index.html') as f:
    page = f.read()
response = 'HTTP/1.0 200 OK\n\n' + "Content-Type: text/html\n\n" + page
conn.sendall(response.encode("utf-8"))

conn.close()
```

* client.py

```
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9523))

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()
```

* index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>My page</title>
</head>
<body>
    <h1>Welcome, friend!</h1>
</body>
</html>
```

## Задание 4

* server.py

```
import socket
import threading

def send_message(sock, msg):
    for client in clients:
        if sock != client:
            client.send(msg)

def handle_client(socket, address, username):
    if not clients.setdefault(socket):
        clients[socket] = username
        print(f'{username}[{address[0]}:{address[1]}] присоединился к чату')
        send_message(socket, f'Пользователь {username} присоединился к чату'.encode())

    while True:
        try:
            message = socket.recv(1024)
            if message.decode('utf-8').find('EXIT FROM CHAT') != -1:
                print(f'{username}[{address[0]}:{address[1]}] покинул чат')
                send_message(socket, f'Пользователь {username} покинул чат'.encode())
                clients.pop(socket)
                break
            send_message(socket, message)
        except ConnectionResetError:
            print(f'{username}[{address[0]}:{address[1]}] неожиданно пропал...')
            send_message(socket, f'Пользователь {username} неожиданно пропал...'.encode())
            break
    socket.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
clients = {}

while True:
  try:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode('utf-8')
    t1 = threading.Thread(target=handle_client, args=(conn, addr, data))
    t1.start()
  except KeyboardInterrupt:
    print('Server stopped')
    break

conn.close()
```

* client.py

```
import threading
import socket
import time

def get_message():
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print(data)
        except socket.error:
            time.sleep(0.5)
            continue

def write_message():
    while True:
        message = input()
        sock.sendto(('[' + name + '] ' + message).encode('utf-8'), server)
        if message == 'EXIT FROM CHAT':
            break
            sock.close()


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9523))

name = input('Введи свой никнэйм: ')
print(f'Привет, {name}! Теперь можешь писать сообщение.')
print('Если захочешь выйти из чата напиши EXIT FROM CHAT\n')

server = '', 9523
sock.sendto((name).encode('utf-8'), server)

thread_send = threading.Thread(target=write_message, args=())
thread_get = threading.Thread(target=get_message, args=())

thread_send.start()
thread_get.start()
```

## Задание 5

* server.py

```
import socket

class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.marks = []

    def serve_forever(self):

        serve_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serve_socket.bind((self.host, self.port))
        serve_socket.listen(10)
        print('hi')
        while True:
            client_socket, address = serve_socket.accept()
            self.serve_client(client_socket)

    def serve_client(self, sock):

        data = sock.recv(4096).decode("utf-8")
        request = self.parse_request(data)
        response = self.handle_request(request)
        sock.send(response.encode())

    def parse_request(self, data):

        request_line = data.split('\r\n')[0]
        words = request_line.split()
        if len(words) == 3:
            try:
                par = data.split('\r\n')[-1]
                param = {}
                for p in par.split("&"):
                    param[p[:p.index('=')]] = p[p.index('=') + 1:]
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": param}
            except:
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": {}}
        else:
            raise Exception('Malformed request line')
        print(req)
        return req

    def parse_headers(self, data):
        lines = data.split('\r\n')[1:]
        headers = {}
        for line in lines:
            parts = line.split(': ')
            headers[parts[0]] = parts[1]
        return headers

    def handle_request(self, request):
        response = f"{request['version']} 200 OK\n\n"

        if request['method'] == 'GET' and request['url'] == "/":
            with open('index.html') as page:
                response += page.read()
        elif request['method'] == 'GET' and request['url'] == "/view":
            body = '<!DOCTYPE html>' \
               '<html lang="ru">' \
               '<head>' \
               '<meta charset="UTF-8">' \
               '<title>Оценки</title>' \
               '</head>' \
               '<body>' \
               '<table align="center" width="20%" border="1">'
            for subject, mark in self.marks:
                body +=f"<tr><td>{subject}</td><td>{mark}</td></tr>"
            body += '</table></body></html>'
            response += body
        elif request['method'] == 'POST':
            self.marks.append((request['parametrs']['subject'], request['parametrs']['mark']))

        return response

if __name__ == '__main__':
    host = 'localhost'
    port = 9523
    name = 'torry-site.ru'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

* index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Marks</title>
    <script>
        function submitForm() {
            let http = new XMLHttpRequest();
            http.open("POST", "http://127.0.0.1:9523/view", true);
            http.setRequestHeader("Content","text/html");
            let params = "?mark=" + document.getElementById("mark").value + "&subject=" + document.getElementById("subject").value;
            http.send(params);
        }

    </script>
</head>
<body>
<form action="" method="post" align="center" onsubmit="submitForm();">
    <br>
    <div>
        <label for="subject">Subject:</label>
        <input type="text" id="subject" name="subject"/>
    </div>
    <br>
    <div>
        <label for="mark">Mark:</label>
        <input type="number" id="mark" name="mark"/>
    </div>
    <br>
    <div>
        <input type="submit">
    </div>
</form>
</body>
</html>
```