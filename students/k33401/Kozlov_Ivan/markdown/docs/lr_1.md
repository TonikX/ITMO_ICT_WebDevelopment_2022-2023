# Welcome to 1 LR
* `client.py` - клиентская часть   
* `server.py` - серверная часть 
## **1 task**

* `server.py`
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
data_from_client = conn.recv(16384)
udata = data_from_client.decode("utf-8")
print("Data: " + udata)
message_to_client = b"Hello, client! \n"
conn.send(message_to_client)
conn.close()
```

* `client.py` 
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8081))
print("Connect to server")
message_to_server = b"Hello, Server!"
conn.send(message_to_server)
data_from_server = conn.recv(16384)
print(data_from_server.decode("utf-8"))
conn.close()
```

## **2 task**

* `server.py`
```python
import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
message_to_client = b"Hello, client! \nWrite three paramets a, b, c with space:"
conn.send(message_to_client)
data_from_client = conn.recv(16384)
parametrs = data_from_client.decode("utf-8")
a = float(parametrs[0])
b = float(parametrs[2])
c = float(parametrs[4])
discr = b ** 2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    message_to_client = "x1 = %.2f \nx2 = %.2f" % (x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    message_to_client = "x = %.2f" % x
else:
    message_to_client = "No roots"

conn.send(message_to_client.encode("utf-8"))

conn.close()
```

* `client.py` 
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8081))
data_from_server = conn.recv(16384)
print(data_from_server.decode("utf-8"))
parametrs = input()
conn.send(parametrs.encode("utf-8"))
data_from_server = conn.recv(16384)
print(data_from_server.decode("utf-8"))

conn.close()
```

## **3 task**

* `server.py`
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
conn.recv(16384)
response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
f = open('index.html','r')
body = f.read()
resp = response_type + headers + body
conn.send(resp.encode("utf-8"))
f.close()
conn.close()
```

* `index.html` - разметка страницы с текстом
```html
<!DOCTYPE html>
<html>
    <head>
        <title>First page</title>
    </head>
    <body>
        <p>Help me, please!</p>
    </body>
</html>
```

## **4 task**
* `server.py`
```python
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(("127.0.0.1", 8081))

clients = []
def send_message():
    while True:
        data, addr = conn.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        for i in clients:
            if i == addr:
                continue
            conn.sendto(data, i)

send_message()
```

* `client.py`
```python
import socket
import threading
import datetime

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(("127.0.0.1", 8081))

def send_mes():
    while True:
        message = input()
        conn.send(message.encode("utf-8"))

def get_m():
    while True:
        message = conn.recv(16384).decode("utf-8")
        print(str(datetime.datetime.now()) + ": " + message)

print("Hello! Write your message:")

thread_send = threading.Thread(target=send_mes, args=())
thread_get = threading.Thread(target=get_m, args=())

thread_send.start()
thread_get.start()
```

## **5 task**

* `server.py`
```python
import socket

class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._database = []

    def serve_forever(self):
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self._conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._conn.bind((self._host, self._port))
        self._conn.listen(10)
        while True:
            client, _ = self._conn.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(4096).decode()
        if not data:
            return
        response = self.handle_request(data)
        client.send(response.encode())


    def parse_request(self, data):
        data = data.replace("\r", "")
        try:
            req = data[:data.index("\n")]
        except ValueError:
            req = data
            return req, "", ""
        if "\n\n" in data:
            headers, body = data[data.index("\n") + 1:].split("\n\n")
        else:
            headers, body = data[data.index("\n") + 1:], ""
        return req, headers, body


    def parse_headers(self, headers):
        headers_dict = {}
        for header in headers.split('\n'):
            if header:
                name = header[:header.index(': ')]
                value = header[header.index(': ') + 1:]
                headers_dict[name] = value
        return headers_dict


    def parse_body(self, body):
        body_dict = {}
        for elem in body.split('&'):
            name = elem[:elem.index('=')]
            value = elem[elem.index('=') + 1:].replace('+', ' ')
            body_dict[name] = value
        return body_dict

    def handle_request(self, data):
        req, headers, body = self.parse_request(data)
        method, url, ver = req.split()
        headers = self.parse_headers(headers)
        response = f"{ver} 200 OK\n\n"
        error_response = f"{ver} 400\n\nBad request"
        if method == 'GET' and url == '/index':
            with open('index.html') as f:
                response += f.read()  
        elif method == 'GET' and url == '/view':
            with open('view.html') as f:
                lines = f.readlines()
            table = [f"<tr><td>{s}</td><td>{g}</td></tr>" for s, g in self._database]
            response += '\n'.join(lines[:8]) + '\n'.join(table) + '\n'.join(lines[8:])
        elif method == 'POST' and url == '/send':
            parsed_body = self.parse_body(body)
            self._database.append((parsed_body['subject'], parsed_body['grade']))
            return response
        else:
            return error_response
        return response

    def kill(self):
        self._conn.close()


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8000
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        serv.kill() 
        raise KeyboardInterrupt


```

* `index.html`
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Task 5</title>
    <script>
        function submitForm() {
            let http = new XMLHttpRequest();
            http.open("POST", "http://127.0.0.1:8000/send", true);
            http.setRequestHeader("Content","text/html");
            let params = "grade=" + document.getElementById("grade").value + "&subject=" + document.getElementById("subject").value;
            http.send(params);
        }
    </script>
</head>
<body>
<form method="post" action="#" onsubmit="submitForm();return false;">
    <label for="subject">Предмет</label>
    <input type="text" name="subject" id="subject"/>
    <label for="grade">Оценка</label>
    <input type="number" name="grade" id="grade"/>
    <input type="submit">
</form>
<a href="/view">Посмотреть таблицу</a>
</body>
</html>
```

* `view.html`
```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Task 5</title>
</head>
<body>
<table align="center" width="20%" border="1">
</table>
<a href="/index">Вернуться ставить оценку</a>
</body>
</html>
```