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