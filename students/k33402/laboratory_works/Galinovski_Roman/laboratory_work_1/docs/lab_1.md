#Лабораторная работа №1 - Работа с сокетами 

##Цель 
* Овладеть практическими навыками и умениями реализации web-серверов и использования сокетов.
##Используемое ПО
* Python 3.10, библиотеки Python: sys, socket.
##Практическое задание:
###Задание №1:
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket

def serverImplementtaion():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.bind(('127.0.0.1', 9796))
    socketVar.listen(1)
    connection, address = socketVar.accept()

    print(f"Server conected to: {address}")

    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"{data.decode('utf-8')} from {address[0]}:{address[1]}")
        connection.send(str.encode(f"Hello, {address[0]}:{address[1]}"))

    connection.close()


if __name__ == "__main__":
    serverImplementtaion()
```

* `client.py`
```python
import socket

def clientImplementation():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.connect(('127.0.0.1', 9796))
    socketVar.send(b'Hello, server!')

    data = socketVar.recv(1024)
    socketVar.close()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    clientImplementation()

###Задание №2:
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера решение квадратного уравнения. Сервер обрабатывает полученные данные и возвращает результат
клиенту. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket
import math

def pifagor(data):
    return int(data[1]) * int(data[2])

def parallelogramArea(data):
    return int(data[1]) * int(data[2]) * math.sin(math.radians(int(data[3])))

def trapezoidArea(data):
    return (1 / 2) * int(data[1]) * int(data[2]) * math.sin(math.radians(int(data[3])))

def mathAreas(_data):
    splitData = _data.split()

    if splitData == "a":
        return pifagor(splitData)
    elif splitData == "b":
        return parallelogramArea(splitData)
    elif splitData == "c":
        return trapezoidArea(splitData)
    else:
        return 0

def server():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9080))
    sock.listen(1)
    connection, address = sock.accept()

    try:
        while 1:
            try:
                connection.settimeout(10)
                data = connection.recv(16384)
                if not data:
                    break
                decData = data.decode("utf-8")
                massage_out = str(mathAreas(decData))
                connection.send(massage_out.encode("utf-8"))
            except socket.error:
                print("connection timed out")
                break
            finally:
                connection.close()
    finally:
        sock.close()

if __name__ == "__main__":
    server()
```

* `client.py`
```python
import socket

def client():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.connect(('127.0.0.1', 9080))

    massage = input("Which formula do you prefer?\n"
                "a is Piffagor theorem\n"
                "b is Parallelogram Area\n"
                "c is Trapezoid Area)\n"
                "Input latter and params: ")
    socketVar.send(massage.encode("utf-8"))
    socketVar.settimeout(1)
    data = socketVar.recv(16384)
    decData = data.decode("utf-8")
    print("Result: " + decData)

if __name__ == "__main__":
    client()
```

###Задание №3:
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html. Обязательно использовать библиотеку socket.

* `server.py`
```python
import socket


def main():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.bind(('localhost', 8080))
    socketVar.listen(1)

    while True:
        conn, addr = socketVar.accept()
        # работа с файлом
        htmlPage = open('index.html')
        htmlContent = htmlPage.read()
        htmlPage.close()

        htmlResponse = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n' + htmlContent

        conn.sendall(htmlResponse.encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    main()
```

* `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Third Task</title>
</head>
<body>
<p>
    "I'm Roman!"
</p>
</body>
</html>
```

###Задание №4:
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов. Обязательно использовать библиотеку threading.

* `server.py`
```python
import socket
import threading

class Chat:
    def __init__(self, ip, host):
        self.socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketVar.bind((ip, host))
        self.socketVar.listen()
        self.clients = {}  # {client:nickname}

    def broadcast(self, message, nickname):
        for client in self.clients.keys():
            client.send(f"{nickname}: {message}".encode())

    def handle_client(self, client):
        while True:
            try:
                message = client.recv(1024).decode()
                self.broadcast(message, self.clients[client])
            except:
                client.close()
                self.broadcast(f'{self.clients[client]} has left the chat...'.encode('utf-8'))
                self.clients.pop(client)
                break

    def receive(self):
        print("Server is running")
        while True:
            client, address = self.socketVar.accept()
            print(f"{str(address)} connected!")
            client.send(b"What is your nickname?")
            nickname = client.recv(1024).decode()
            self.clients[client] = nickname
            self.broadcast(f"{nickname} has connected to the chat", "Server")
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    Chat("127.0.0.1", 9980).run()
```

* `client.py`
```python
import socket
import threading


class Client:
    def __init__(self, ip, port):
        self.nickname = ""
        self.socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketVar.connect((ip, port))

    def receive(self):
        while True:
            try:
                message = self.socketVar.recv(1024).decode()
                if message == "What's your nickname?":
                    self.socketVar.send(self.nickname.encode())
                else:
                    print(message)
            except:
                print("Error...")
                self.socketVar.close()
                break

    def send(self):
        while True:
            message = input()
            self.socketVar.send(message.encode())

    def start(self):
        self.nickname = input("Enter your nickname: ")
        receiveThread = threading.Thread(target=self.receive)
        receiveThread.start()

        sendThread = threading.Thread(target=self.send)
        sendThread.start()


if __name__ == "__main__":
    Client("127.0.0.1", 9980).start()
```

###Задание №5:
Написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket, который может:
`принять и записать информацию о дисциплине и оценке по дисциплине`,
`отдать информацию обо всех оценках по дисциплине в виде html-страницы.`

* `server.py`
```python
import socket

class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.marks = []

    def serveForever(self):

        serveSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serveSocket.bind((self.host, self.port))
        serveSocket.listen(10)
        print('hi')
        while True:
            clientSocket, address = serveSocket.accept()
            self.serveClient(clientSocket)

    def serveClient(self, sock):

        data = sock.recv(4096).decode("utf-8")
        request = self.parseRequest(data)
        response = self.handleRequest(request)
        sock.send(response.encode())

    def parseRequest(self, data):

        requestLine = data.split('\r\n')[0]
        words = requestLine.split()
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

    def parseHeaders(self, data):
        lines = data.split('\r\n')[1:]
        headers = {}
        for line in lines:
            parts = line.split(': ')
            headers[parts[0]] = parts[1]
        return headers

    def handleRequest(self, request):
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
    port = 9889
    name = 'detribesite.ru'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serveForever()
    except KeyboardInterrupt:
        pass
```