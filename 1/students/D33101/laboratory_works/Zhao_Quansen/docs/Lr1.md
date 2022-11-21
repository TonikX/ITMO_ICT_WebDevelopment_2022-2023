# Лабораторная работа 1

## Work 1

* `server.py`
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4245))

while True:
   data, addr = s.recvfrom(1024)
   print(f"Получено от {addr}\nЗапрос: {data.decode()}\n")
   if data == b"Hello, server":
       s.sendto(b"Hello, client", addr)
   else:
       s.sendto("Я не понимаю...".encode(), addr)

s.close()
print("Сервер закончил работу!")
```

* `client.py`
```python
import socket
 
socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 4245)
 
message = input("Ваше сообщение: ")
socket_.sendto(message.encode(), server_addr)
response, server_addr = socket_.recvfrom(1024)
print(f'Ответ от сервера: {response.decode()}\n')
socket_.close()
```
##Work 2

*`server.py`
```python
import socket
import math

tcp_socket_host = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket_host.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
tcp_socket_host.bind(('127.0.0.1', 4245))
tcp_socket_host.listen()

while True:
    client, addr = tcp_socket_host.accept()
    data = [float(i) for i in client.recv(1024).decode().split(',')]
    a = data[0]
    b = data[1]
    c = data[2]
    dis = b ** 2 - 4 * a * c
    
    if dis > 0:
        x1 = (-b + math.sqrt(dis)) / (2 * a)
        x2 = (-b - math.sqrt(dis)) / (2 * a)
        client.send(f'x1 = {x1}\nx2 = {x2}'.encode())
    elif dis == 0:
        x = -b / (2 * a)
        client.send(f"x = {x}".encode())
    else:
        client.send("Корней нет".encode())
```

*`client.py`
```python
from socket import *

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

print("Решение квадратного уравнения.")
print("Введите коэффициенты для уравнения: ax^2 + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
socket.send(f'{a},{b},{c}'.encode())
recv_data = socket.recv(1024)
print(f'Решение: \n{recv_data.decode()}')

socket.close()
```

##Work 3

*`sever.py`
```python
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 4245))
server_socket.listen()

while True:
    client, address = server_socket.accept()
    req = client.recv(1024).decode()
    code = open('index.html')
    res = 'HTTP/1.0 200 OK\n\n' + code.read()
    code.close()
    if req == 'адрес страницы':
        client.send(f'Адрес страницы: http://127.0.0.1:4245'.encode())
    else:
        client.sendall(res.encode())
    client.close()
```

*`client.py`
```python
from socket import *

socket = socket(AF_INET,SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

socket.send('адрес страницы'.encode())
adress = socket.recv(1024)
print(adress.decode())

socket.close()
```

##Work 4

*`server.py`
```python
import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 4245))
server.listen()

conns = []
names = []

def print_msg(message, name = 'Сервер', conn_not_send = ''):
    for conn in conns:
        if conn != conn_not_send:
            conn.send(f'{name} говорит > {message.decode()}'.encode())
        
def control(conn):
    while True:
        try:
            message = conn.recv(1024)
            print_msg(message, names[conns.index(conn)], conn)
        except:
            index = conns.index(conn)
            conns.remove(conn)
            conn.close()
            nickname = names[index]
            print_msg(f'{nickname} отключился.'.encode())
            names.remove(nickname)
            break
        
def get():
    while True:
        conn, addr = server.accept()

        conn.send('регистрация'.encode())
        name = conn.recv(1024).decode()
        names.append(name)
        conns.append(conn)

        conn.send('Подключился к серверу!\n'.encode())
        print_msg(f"{name} подключился!-->".encode())
        
        thread = threading.Thread(target=control, args=(conn,))
        thread.start()

get()
```
*`client.py`
```python
import socket
import threading

nickname = input("Имя пользователя: ")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

def get():
    while True:
        try:
            message = socket.recv(1024).decode()
            if message == 'регистрация':
                socket.send(nickname.encode())
            else:
                print(message)
        except:
            break
        
def send():
    while True:
        msg = input('')
        if msg == 'out':
            socket.close()
            break
        socket.send(msg.encode())

get_thread = threading.Thread(target = get)
get_thread.start()

send_thread = threading.Thread(target = send)
send_thread.start()
```

##Work 5
*`server.py`
```python
import socket

lessons = [
  {'name': 'Python', 'desc': 'Client/Server', 'marks' : [4,5]}
]

def post_func(post_msg):
  info = post_msg.split('&')
  return [info[0][7:], info[1][5:], [int(i) for i in info[2][6:].split('%2C')]]

def get():
  html = '<ol>'
  for lesson in lessons:
    html += '<li>'
    html += f'<h1>Lesson: {lesson["name"]}</h1>'
    for mark in lesson['marks']:
      html += f'<p>grade: {mark}</p>'
    html += '</li>'
  html += '</ol>'
  return html

def add():
  form = """
  <form action="/" method="post">
    <P>Lesson: </p>
    <input type="text" name="lesson" value="math"/>
    <P>Description: </p>
    <input type="text" name="desc" value="numbers"/>
    <P>Grades: </p>
    <input type="text" name="marks" value="5,5,5"/>
    <br/>
    <input type="submit" value="Add lesson"/>
  </form>"""
  return form

def start_server():
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('127.0.0.1', 4245))
  server.listen()
  
  while True:
    client, addr = server.accept()

    with client:
      request = client.recv(1024).decode()
      method = request.split(' ')[0]
      message = request.split(' ')[1][1:-1]
      setting = 'HTTP/1.1 200 OK\r\nContent-Type: text.html; charset=UTF-8\r\n\r\n'
      html = '<html><head><title>Website</title></head><body>'
      html += """
      <form method="get">
        <input type="submit" formaction="add" value="Add" />
        <input type="submit" formaction="get" value="Show" />
      </form>
      """
      if method == 'GET':
        if message == 'get':
          html += get()
        elif message == 'add':
          html += add()
      else:
        post = post_func(request.split(' ')[-1].split('\r\n\r\n')[1])
        lessons.append({'name': post[0], 'desc': post[1], 'marks' : post[2]})
      
      html += "</body></html>"
      client.send(setting.encode('utf-8') + html.encode('utf-8'))  
      
start_server();
```