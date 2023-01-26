# Лабораторная работа №1

## Задача №1
Серверная часть приложения
* `server.py`
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 8080))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall('Hello, client.'.encode('utf-8'))
    print(data.decode('utf-8'))
conn.close()
```
Клиентская часть приложения
* `client.py`
```python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 8080))
s.sendall('Hello, server.'.encode('utf-8'))
data = s.recv(1024)
print(data.decode('utf-8'))
s.close()
```

## Задача №2
Серверная часть приложения
* `server.py`
```python
from math import sqrt
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 3030))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        break
    coefs = data.decode('utf-8').split(',')
    for i in range(len(coefs)):
        coefs[i] = int(coefs[i])

    d = coefs[1]**2 - 4*coefs[0]*coefs[2]
    if d < 0:
        conn.sendall('No solutions'.encode('utf-8'))
    elif d == 0:
        result = 'Equations`s roots: ' + str(round(-coefs[1]/(2*coefs[0]),3))
        conn.sendall(result.encode('utf-8'))
    else:
        result = 'Quadratic equations`s roots: ' + str(round((-coefs[1]-sqrt(d))/(2*coefs[0]),3)) + ' ' + str(round((-coefs[1]+sqrt(d))/(2*coefs[0]),3))
        conn.sendall(result.encode('utf-8'))
conn.close()
```
Клиентская часть приложения
* `client.py`
```python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 3030))
print('Enter quadratic equation`s coefficients')
a, b, c = map(int, input().split())
s.sendall((str(a)+','+str(b)+','+str(c)).encode('utf-8'))
answer = s.recv(1024)
print(answer.decode('utf-8'))
s.close()
```

## Задача №3
Серверная часть приложения
* `server.py`
```python
import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8080))
    s.listen(1)

    while True:
        conn, addr = s.accept()
        # работа с файлом
        html_page = open('index.html')
        html_content = html_page.read()
        html_page.close()

        html_response = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n' + html_content

        conn.sendall(html_response.encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    main()
```
Html страница приложения
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
Серверная часть приложения
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
            if message.decode('utf-8').find('bye besties') != -1: #клиент покидает
                send_to_chat(cl_sock, message)
                break
            elif message.decode('utf-8').find('Error') != -1:
                break
            send_to_chat(cl_sock, message)  #отправляем сообщение участникам чата
        except socket.error:
            print(f'Client {cl_addr[0]}:{cl_addr[1]} left all of the sudden')
            break

    print (f'Client {cl_addr[0]}:{cl_addr[1]} left the chat :(')
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
Клиентская часть приложения
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

alias = input("Enter your nickname: ")
print('If you want to leave the chat type `bye besties` ')
rt = threading.Thread(target = recive)
rt.start()


while True:
    try:
        message = input()
        s.sendall((f'{alias} :: {message}').encode('utf-8'))
        if message == 'bye besties':
            print('You have left the chat')
            shutdown = True
            break
    except:
        s.sendall('Error'.encode('utf-8'))
        print('Error. Disconnected')
        shutdown = True
        break
s.close()
```