## _Крамаренко Ирина, K33422_
# Лабораторная работа 1
## Задание 1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера. Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно отобразиться у клиента.
Реализовано с помощью протокола UDP.
### server
```py
import socket
host = 'localhost'
port = 9090
addr = (host, port)
s_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_server.bind(addr)
while True:
    rcvd = s_server.recvfrom(1024)
    print("Message from client: {}".format(rcvd[0].decode("utf-8")))
    s_server.sendto(str.encode("Hello, client"), rcvd[1])
```
### client
```py
import socket
s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_client.sendto(str.encode('Hello, server'), ('localhost', 9090))
rcvd = s_client.recvfrom(1024)
print("Message from Server: {}".format(rcvd[0].decode("utf-8")))
```
## Задание 2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у сервера выполнение математической операции, параметры, которые вводятся с клавиатуры. Сервер обрабатывает полученные данные и возвращает результат клиенту. 
Поиск площади параллелограмма.
Реализовано с помощью протокола TCP.
### server
```py
import socket
host = 'localhost'
port = 9090
addr = (host, port)
def main():
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.bind(addr)
    s_server.listen(1)
    while True:
        print("Ожидание клиентской ссылки...")
        s_client, client_addr = s_server.accept()
        print("Клиентское соединение успешно")
        while True:
            rcvd = s_client.recv(1024)
            print(rcvd.decode("utf-8"))
            if rcvd:
                a, height = map(lambda x: int(x), rcvd.split())
                square = a * height
                s_client.send(str(square).encode("utf-8"))
            else:
                break
        s_client.close()
    s_server.close()
if __name__ == "__main__":
    main()
```
### client
```py
import socket
def main():
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_client.connect(('localhost', 9090))
    client_msg = input("Введите длину стороны и высоты параллелограмма:")
    s_client.send(client_msg.encode("utf-8"))
    rcvd = s_client.recv(1024)
    print("Площадь параллелограмма:" + rcvd.decode("utf-8"))
    s_client.close()
if __name__ == "__main__":
    main()
```
## Задание 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ клиент получает http-сообщение, содержащее html-страницу, которую сервер подгружает из файла index.html. 
### server
```py
addr = (host, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(1)
sock, client_addr = sock.accept()
sock.recv(1024)
response_type = "HTTP/1.1 200 OK\n"
headers = "Content-Type: text/html\n\n"
body = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form action="">
Имя: <input type="text" name="name"><br>
Фамилия: <input type="text" name="surname"><br>
Введите логин: <input type="text" name="login">
</form>
</body>
</html>
"""
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
sock.close()
```
### client
```py
import socket
s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_client.connect(('localhost', 9090))
s_client.send('Hello, server'.encode("utf-8"))
rcvd = s_client.recv(1024)
print(rcvd.decode("utf-8"))
s_client.close()
```
## Задание 4
Реализовать двухпользовательский или многопользовательский чат. Реализация многопользовательского часа позволяет получить максимальное количество баллов.
Реализовано с помощью протокола TCP.
### server
```py
import socket
import threading
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
print("Сервер подключен")
server.listen(10)
clients = []
end = []
def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)
def recv(client):
    while True:
        try:
            rcvd = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            break
        print(rcvd.decode("utf-8"))
        for cl in clients:
            if cl != client:
                cl.send(rcvd)
def send():
    while True:
        print("")
        to_send = input("")
        print()
        if to_send == "exit":
            break
        print("Отправить всем: %s"% to_send)
        for client in clients:
            client.send(f"Сервер: {to_send}".encode("utf-8"))
def threads():
    while True:
        for cl in clients:
            if cl in end:
                continue
            index = threading.Thread(target=recv, args=(cl,))
            index.start()
            end.append(cl)
thread1 = threading.Thread(target=threads, name="input")
thread1.start()
thread2 = threading.Thread(target=send, name="out")
thread2.start()
thread3 = threading.Thread(target=accept, name="accept")
thread3.start()
thread2.join()
for client in clients:
    client.close()
print("Сервер отключен")
```
### client
```py
import socket
import threading
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
addr = (host, port)
username = input("Введите свой ник:")
client.connect(addr)
print("Подключение к серверу выполнено")
print("Введите exit, чтобы закрыть соединение с сервером")
def send():
    while True:
        to_send = input("Введите сообщение: ")
        print()
        if to_send == "exit":
            # print("Соединение с сервером закрыто")
            break
        client.send(f"{username}: {to_send}".encode("utf-8"))
        print("%s:%s"% (username, to_send))
def recv():
    while True:
        rcvd = client.recv(1024)
        print("\n" + rcvd.decode("utf-8"))
thread1 = threading.Thread(target=recv, name="input")
thread2 = threading.Thread(target=send, name="out")
thread1.start()
thread2.start()
thread2.join()
print("Соединение с сервером закрыто")
client.close()
```
## Задание 5
Необходимо написать простой web-сервер для обработки GET и POST http запросов средствами Python и библиотеки socket.
### server
```py
import socket
import sys
class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._subjs = []
        self._marks = []
    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()
            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()
    def serve_client(self, conn):
        data = conn.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(conn, resp)
    def parse_request(self, data):
        lines = data.split('\r\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body
    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as file:
                    resp += file.read()
                return resp
            if method == 'POST':
                resp = "HTTP/1.1 204 OK\n\n"
                params = body.split('&')
                for a in params:
                    if a.split('=')[0] == 'subj':
                        self._subjs.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        self._marks.append(a.split('=')[1])
                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, m in zip(self._subjs, self._marks):
                    resp += f"<li>Subject: {s}, Grade: {m}</li>"
                resp += "</ol></body></html>"
                return resp
    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))
if __name__ == '__main__':
    host ='127.0.0.1'
    port = 8000
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
### index
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Journal</title>
</head>
<body>
    <p>Enter the name of the discipline and the grade
        <form action="/" method="post">
            <label for="subject">Subject:</label>
            <input type="text" name="subject" id="subject"/>
            <label for="grade">Grade:</label>
            <input type="number" name="grade" id="grade"/>
            <button>Submit</button>
        </form>
    </p>
</body>
</html>
```