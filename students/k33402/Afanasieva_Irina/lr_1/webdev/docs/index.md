#Лабораторная работа 1

##Работа с сокетами

##Задание 1
Реализовать клиентскую и серверную часть приложения. Клиент отсылает серверу
сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

Обязательно использовать библиотеку `socket`

Реализовать с помощью протокола `UDP`

####Клиентская часть

```
import socket

my_socket = socket.socket(socket.SOCK_DGRAM)
my_socket.connect(("127.0.0.10", 12400))
msg = "Hello, server!"
my_socket.send(msg.encode("utf-8"))
data = my_socket.recv(16384)
print(data.decode("utf-8"))
my_socket.close() 
```

Создаем сокет `my_socket` и подключаемся к серверу:
```
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 12400))
```
Отправляем на сервер сообщение "Hello, server!":
```
msg = "Hello, server!"
my_socket.send(msg.encode("utf-8"))
```
Получаем сообщение от сервера, печатаем его и закрываем соединение:
```
data = my_socket.recv(16384)
print(data.decode("utf-8"))
my_socket.close() 
```
####Серверная часть
```
import socket

my_socket = socket.socket(socket.SOCK_DGRAM)
my_socket.bind(("127.0.0.10", 12400))
my_socket.listen(10)

sock, address = my_socket.accept()
data = sock.recv(16384)
data = data.decode("utf-8")
print(data)
msg = "Hello, client!"
sock.send(msg.encode("utf-8"))
my_socket.close()
```

Создаем сокет `my_socket` и с помощью метода `.listen()` запускаем режим прослушивания:

```
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("127.0.0.1", 12400))
my_socket.listen(10)
```
Получаем сообщение от клиента и печатаем его:
```
sock, address = my_socket.accept()
data = sock.recv(16384)
data = data.decode("utf-8")
print(data)
```
Отправляем клиенту сообщение "Hello, client!" и закрываем соединение:
```
msg = "Hello, client!"
sock.send(msg.encode("utf-8"))
my_socket.close()
```


##Задание 2
Реализовать клиентскую и серверную часть приложения. Клиент запрашивает у
сервера решение Теоремы Пифагора, параметры которой вводятся с
клавиатуры. Сервер обрабатывает полученные данные и возвращает результат
клиенту.

Обязательно использовать библиотеку `socket`

Реализовать с помощью протокола `TCP`
####Клиентская часть
```
# Variant a. - теорема пифагора
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 12400))

# Два прохода цикла, тк 2 вводных числа
for _ in range(2):
    print(my_socket.recv(16384).decode())  # Сообщение от сервера
    inp = input(">> ")  # Вводимые катеты
    my_socket.send(inp.encode())  # Отправка на сервер

print(my_socket.recv(16384).decode())
my_socket.close()
```

Создаем сокет `my_socket` и подключаемся к серверу:
```
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 12400))
```
В цикле делаем два прохода, получая сообщения от сервера и посылая вводные данные:
```
for _ in range(2):
    print(my_socket.recv(16384).decode())  # Сообщение от сервера
    inp = input(">> ")  # Вводимые катеты
    my_socket.send(inp.encode())  # Отправка на сервер
```
Получаем и печатаем результат, полученный с сервера. Закрываем соединение:
```
print(my_socket.recv(16384).decode())
my_socket.close()
```

####Серверная часть
```
import socket
import math

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("127.0.0.1", 12400))

my_socket.listen(10)

sock, address = my_socket.accept()
sock.send("Input a:".encode())
a = int(sock.recv(16384).decode())  # Первый катет
sock.send("Input b:".encode())
b = int(sock.recv(16384).decode())  # Второй катет
c = a * a + b * b
result = math.sqrt(c)
sock.send(f"The result is:\n {result}".encode())
my_socket.close()
```

Создаем сокет `my_socket` и с помощью метода `.listen()` запускаем режим прослушивания:

```
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("127.0.0.1", 12400))
my_socket.listen(10)
```
Сервер отправляет клиенту сообщения для запроса вводных данных и принимает их:
```
sock, address = my_socket.accept()
sock.send("Input a:".encode())
a = int(sock.recv(16384).decode()) 
sock.send("Input b:".encode())
b = int(sock.recv(16384).decode()) 
```
Расчет длины гипотенузы из двух катетов по Теореме Пифагора:
```
c = a * a + b * b
result = math.sqrt(c)
```
Сервер отправляет результат расчета клиенту и закрывает соединение:
```
sock.send(f"The result is:\n {result}".encode())
my_socket.close()
```
##Задание 3
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

Обязательно использовать библиотеку `socket`

```
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(('127.0.0.1', 14900))
my_socket.listen(10)


def main():
    while True:
        try:
            client, _ = my_socket.accept()
            client.recv(4096)
            response_type = "HTTP/1.0 200 OK\n"
            headers = "Content-Type: text/html\n\n"
            with open("index.html", "r") as f:
                body = f.read()
            resp = response_type + headers + body
            client.send(resp.encode())
            client.close()
        except KeyboardInterrupt:
            my_socket.close()
            break


if __name__ == '__main__':
    main()
```

##Задание 4
Реализовать двухпользовательский или многопользовательский чат. Реализация
многопользовательского часа позволяет получить максимальное количество
баллов.

Обязательно использовать библиотеку `socket`

Обязательно использовать библиотеку `threading`

Реализовать с помощью протокола `TCP`


####Клиентская часть
```
import socket
import sys
from threading import Thread


class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _send(self):
        # Многопоточная функция для отправки сообщений
        while True:
            try:
                msg = input()
                if msg:
                    self.conn.send(f"{self.username}: {msg}".encode())
            except (KeyboardInterrupt, EOFError):
                self.conn.close()
                sys.exit(0)

    def _recieve(self):
        # Многопоточная функция для получения сообщений
        while True:
            try:
                msg = self.conn.recv(16384).decode()
                if msg:
                    print(msg)
            except KeyboardInterrupt:
                self.conn.close()
                sys.exit(0)
            except ConnectionError:
                # Ошибка подключения
                print("Connection error")
                self.conn.close()
                sys.exit(1)

    def run(self):
        # Подключение
        self.conn.connect((self.host, self.port))
        # Запуск многопоточной функции
        Thread(target=self._send).start()
        Thread(target=self._recieve).start()


if __name__ == '__main__':
    u = input("Your username: ")
    print(f"Hello {u}")
    print("Connecting to server...")
    client = ChatClient('127.0.0.1', 14900, u)
    client.run()
```

####Серверная часть
```
import socket
import sys
from threading import Thread


class ChatServer:

    def __init__(self, host: str, port: int):
        self.clients = []
        self.host = host
        self.port = port
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _shutdown(self):
        for sock in self.clients:
            sock.close()
        self.conn.close()
        sys.exit(0)

    def _client_broadcast(self, message: bytes, sender: socket.socket) -> None:
        # Отправка сообщения клиента другим клиентам
        for sock in self.clients.copy():
            if sock != sender:
                try:
                    sock.send(message)
                except OSError:
                    # Клиент отключился
                    print("Someone disconnected")
                    self.clients.remove(sock)

    def _client_listen(self, sock: socket.socket) -> None:
        # Ожидание сообщения от клиента
        sock.settimeout(30)
        while True:
            try:
                message = sock.recv(16384)
                print(message.decode())
                self._client_broadcast(message, sock)
            except OSError:
                sock.close()
                break

    def _main(self) -> None:
        # Запуск сервера
        self.conn.bind((self.host, self.port))
        self.conn.listen(10)
        while True:
            try:
                # Подтверждение подключения
                sock, address = self.conn.accept()
                print(f"Connection at {address}")
                # Создание потока для клиентов
                self.clients.append(sock)
                Thread(target=self._client_listen, args=(sock,)).start()
            except KeyboardInterrupt:
                self._shutdown()

    def run(self) -> None:
        # Упаковщик для запуска многопоточной функции _main()
        Thread(target=self._main).start()


if __name__ == '__main__':
    print("Starting server...")
    server = ChatServer('127.0.0.1', 14900)
    server.run()
    print("Server started")
```

##Задание 5
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket.

Задание: сделать сервер, который может:

● Принять и записать информацию о дисциплине и оценке по дисциплине.

● Отдать информацию обо всех оценах по дсициплине в виде html-страницы.
```
import socket


class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.grade = []


    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        while True:
            client_socket, _ = sock.accept()
            self.serve_client(client_socket)


    def serve_client(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        request = self.parse_request(data)
        response = self.handle_request(request)
        if response:
            client_socket.send(response.encode('utf-8'))
            client_socket.close()


    def parse_request(self, data):
        data_split = data.split('\r\n')
        print(f"data split : {data_split}")
        headers = data_split[0].split()
        print(f"Headers : {headers}")
        body = data_split[-1]
        request = dict()

        if len(headers) == 3:

            request.update(
                {"method": headers[0], "url": headers[1], "version": headers[2]})

            if "&" in body:
                parametre = body.split("&")
                request.update({"parametrs": parametre})
                return request
            else:
                request.update({"parametrs": {}})
                return request
        else:
            raise Exception("Malformed request line")


    def handle_request(self, request):
        print(request)
        response = f"{request['version']} 200 OK\n\n"
        if request["url"] == "/":
            if request["method"] == "POST":
                 self.grade.extend(request["parametrs"])
            if request["method"] == "GET" or "POST":
                with open('insert.html') as f:
                    response += f.read()
                    return response
        if request["url"] == "/journal":
            response += "<html><head><title>List grades</title></head><body>"
            for s in self.grade:
                response += f"<p>{s} </p>"
            response += "</body></html>"
            return response


if __name__ == "__main__":
    host = 'localhost'
    port = 3968
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass
```

Параметры сервера:

```
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.grade = []
```

Запуск сервера на сокете, обработка входящих соединений:

```
    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        while True:
            client_socket, _ = sock.accept()
            self.serve_client(client_socket)
```

Обработка клиентского подключения:

```
    def serve_client(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        request = self.parse_request(data)
        response = self.handle_request(request)
        if response:
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
```

Функция для обработки заголовка http+запроса:

```
    def parse_request(self, data):
        data_split = data.split('\r\n')
        print(f"data split : {data_split}")
        headers = data_split[0].split()
        print(f"Headers : {headers}")
        body = data_split[-1]
        request = dict()

        if len(headers) == 3:

            request.update(
                {"method": headers[0], "url": headers[1], "version": headers[2]})

            if "&" in body:
                parametre = body.split("&")
                request.update({"parametrs": parametre})
                return request
            else:
                request.update({"parametrs": {}})
                return request
        else:
            raise Exception("Malformed request line")
```

Функция для обработки url в соответствии с нужным методом:

```
    def handle_request(self, request):
        print(request)
        response = f"{request['version']} 200 OK\n\n"
        if request["url"] == "/":
            if request["method"] == "POST":
                 self.grade.extend(request["parametrs"])
            if request["method"] == "GET" or "POST":
                with open('insert.html') as f:
                    response += f.read()
                    return response
        if request["url"] == "/journal":
            response += "<html><head><title>List grades</title></head><body>"
            for s in self.grade:
                response += f"<p>{s} </p>"
            response += "</body></html>"
            return response
```