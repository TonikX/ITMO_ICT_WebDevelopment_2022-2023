# Tasks 1-3
Для задач с 1 по 3 включительно отдельно вынесены два класса, реализующие серверную и клиентскую части:

_server.py_
```python
import socket


class Server:
    def __init__(self, protocol_type: str):
        if protocol_type == "UDP":
            self.socket = self.__create_UDP_socket()
        elif protocol_type == "TCP":
            self.socket = self.__create_TCP_socket()
            
    def __create_TCP_socket(self) -> socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def __create_UDP_socket(self):
        sock = socket.socket()
        sock.bind((socket.gethostname(), 1234))
        sock.listen(1)

        return sock

    def send_data_to_client(self, client_socket: socket.socket, data: str):
        client_socket.send(data.encode())

    def get_data_from_client(self, client_socket: socket.socket) -> str:
        encoded_data = client_socket.recv(1024)
        data = encoded_data.decode("utf-8")

        return data

    def accept_connection(self) -> (socket, tp.Any):
        return self.socket.accept()
```

_client.py_
```python
import socket


class Client:
    def __init__(self, protocol_type: str):
        if protocol_type == "UDP":
            self.socket = self.__create_UDP_socket()
        elif protocol_type == "TCP":
            self.socket = self.__create_TCP_socket()
            
    def __create_TCP_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((socket.gethostname(), 1234))

        return sock

    def __create_UDP_socket(self):
        sock = socket.socket()
        sock.connect((socket.gethostname(), 1234))

        return sock
            
    def send_data_to_server(self, data: str):
        self.socket.send(data.encode())

    def get_data_from_server(self) -> str:
        encoded_data = self.socket.recv(1024)
        data = encoded_data.decode("utf-8")

        return data
```

---

## Task 1
#### Задание
Реализовать клиентскую и серверную часть приложения, используя проотокол UDP.
Клиент отсылает серверу сообщение «Hello, server». Сообщение должно отразиться на стороне сервера.
Сервер в ответ отсылает клиенту сообщение «Hello, client». Сообщение должно
отобразиться у клиента.

#### Реализация

_server.py_
```python
from Lr1.server import Server


class FirstTaskServer(Server):
    def start(self):
        # create connection
        client_socket, address = self.accept_connection()
        self.send_data_to_client(client_socket, "Hello, client")

        client_data = self.get_data_from_client(client_socket)
        print(client_data)

        client_socket.close()
        self.socket.close()
```

_client.py_
```python
from Lr1.client import Client


class FirstTaskClient(Client):
    def start(self):
        self.send_data_to_server("Hello, server!")

        server_data = self.get_data_from_server()
        print(server_data)

        self.socket.close()
```

#### Запуск
```python
server = FirstTaskServer("UDP")
server.start()

client = FirstTaskClient("UDP")
client.start()
```

---

## Task 2
#### Задание
Реализовать клиентскую и серверную часть приложения с помощью протокола TCP. 
Клиент запрашивает у сервера расчет площади параллелограмма, задавая с клавиатуры координаты двух векторов на которых он построен в трехмерной системе координат. 
Сервер обрабатывает полученные данные и возвращает результат
клиенту.

#### Реализация

_server.py_
```python
from Lr1.server import Server
import typing as tp


class SecondTaskServer(Server):
    def start(self):
        client_socket, address = self.accept_connection()

        while not self.area:
            while len(self.vectors) < 2:
                if len(self.vectors) == 0:
                    self.send_data_to_client(client_socket, "First vector")
                else:
                    self.send_data_to_client(client_socket, "Second vector")

                data = self.get_data_from_client(client_socket)
                self._set_vector_from_data(data)

            self._set_area()
            client_socket.send(str(self.area).encode())

        client_socket.close()
        self.socket.close()
        
    def _set_vector_from_data(self, data: str):
        coords = tuple(map(float, data.split()))
        self.vectors.append(coords)

    def _set_area(self):
        x = self.vectors[0][1] * self.vectors[1][2] - self.vectors[0][2] * self.vectors[1][1]
        y = self.vectors[0][0] * self.vectors[1][2] - self.vectors[0][2] * self.vectors[1][0]
        z = self.vectors[0][0] * self.vectors[1][1] - self.vectors[0][1] * self.vectors[1][0]

        self.area = (x**2 + y**2 + z**2)**0.5

    def __init__(self, protocol_type: str):
        super().__init__(protocol_type)
        self.vectors: tp.List[tp.Tuple[float, ...]] = []
        self.area = 0.0
```

_client.py_
```python
from Lr1.client import Client


class SecondTaskClient(Client):
    def start(self):
        first_vector = input("Enter first vector's coordinates x, y, z: ")
        second_vector = input("Enter second vector's coordinates x, y, z: ")

        while True:
            data = self.get_data_from_server()
            if data == "First vector":
                self.send_data_to_server(first_vector)
            elif data == "Second vector":
                self.send_data_to_server(second_vector)
            else:
                print(data)
                break

        self.socket.close()
```

#### Запуск
```python
server = SecondTaskServer("TCP")
server.start()

client = SecondTaskClient("TCP")
client.start()
```

---

## Task 3
#### Задание
Реализовать серверную часть приложения. Клиент подключается к серверу. В ответ
клиент получает http-сообщение, содержащее html-страницу, которую сервер
подгружает из файла index.html.

#### Реализация
_server.py_
```python
class ThirdTaskServer(Server):
    def start(self):
        client_socket, address = self.accept_connection()

        self._get_content()
        self._send_page_to_client(client_socket)

        client_socket.close()
        self.socket.close()

    def _get_content(self):
        with open("index.html", "r") as file:
            self.content = file.read()

    def _send_page_to_client(self, client_socket):
        page_info = f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{self.content}'
        self.send_data_to_client(client_socket, page_info)

    def __init__(self, protocol_type: str):
        super().__init__(protocol_type)
        self.content = ""
```

#### Запуск
```python
server = ThirdTaskServer("TCP")
server.start()
```

---

# Task 4
#### Задание
Реализовать многопользовательский чат.

#### Реализация
_server.py_
```python
import socket
import threading
import typing as tp


class User:
    def __init__(self, name: str, sock: socket.socket):
        self.name = name
        self.sock = sock


class ChatServer:
    def __init__(self):
        self.alive = True
        self.sock = self.__create_tcp_socket()
        self.users: tp.List[User] = []

    def __create_tcp_socket(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen()

        return sock

    def __send_data_to_user(self, user_socket: socket.socket, data: str):
        try:
            user_socket.send(data.encode())
        except:
            pass

    def __get_data_from_user(self, user_socket: socket.socket) -> str:
        data = ""
        try:
            data = user_socket.recv(1024).decode()
        finally:
            return data

    def __remove_user_from_chat(self, user: User):
        user.sock.close()
        self.users.remove(user)
        self.send_broadcast_message(None, f'{user.name} has left the chat')

    def switch_off(self):
        self.alive = False
        for user in self.users:
            self.__send_data_to_user(user.sock, "!END")
            user.sock.close()
        self.sock.close()

    def send_broadcast_message(self, author: tp.Optional[str], text: str):
        if author is None:
            data = f"{text}"
        else:
            data = f"{author}: {text}"

        for user in self.users:
            self.__send_data_to_user(user.sock, data)

    def handle_connection(self, user: User):
        try:
            while self.alive:
                message = self.__get_data_from_user(user.sock)
                if message != "!QUIT":
                    self.send_broadcast_message(user.name, message)
                else:
                    break
        finally:
            self.__remove_user_from_chat(user)

    def serve_forever(self):
        while self.alive:
            user_socket, _ = self.sock.accept()

            self.__send_data_to_user(user_socket, "Enter Username")
            username = self.__get_data_from_user(user_socket)

            user = User(username, user_socket)
            self.users.append(user)
            self.send_broadcast_message(None, f"{username} has connected to the chat")

            thread = threading.Thread(target=self.handle_connection, args=(user,))
            thread.start()

    def start(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            self.switch_off()
```

_client.py_
```python
import threading


class ChatClient:
    def __init__(self):
        self.username = ""
        self.alive = True
        self.sock = self.__create_tcp_socket()

    def __create_tcp_socket(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((socket.gethostname(), 1234))

        return sock

    def __send_data_to_server(self, data: str):
        if self.alive:
            self.sock.send(data.encode())

    def __get_data_from_server(self) -> str:
        return self.sock.recv(1024).decode()

    def __left_from_server(self):
        self.alive = False
        self.sock.close()

        print("You have left the chat")

    def receive(self):
        try:
            while self.alive:
                message = self.__get_data_from_server()
                if message == "Enter Username":
                    self.__send_data_to_server(self.username)
                elif message == "!END":
                    print("The server was interrupted")
                    break
                else:
                    print(message)
        finally:
            self.__left_from_server()

    def send(self):
        while self.alive:
            message = input()
            self.__send_data_to_server(message)

            if message == "!QUIT":
                self.alive = False

    def start(self):
        self.username = input("Enter username: ")

        get_thread = threading.Thread(target=self.receive)
        get_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()
```

#### Запуск
```python
# запустить сервер
ChatServer().start()

# создать пользователя
ChatClient().start()
```

---

# Task 5
#### Задание
Необходимо написать простой web-сервер для обработки GET и POST http
запросов средствами Python и библиотеки socket. Сервер должен уметь:
- Принять и записать информацию о дисциплине и оценке по дисциплине.
- Отдать информацию обо всех оценах по дсициплине в виде html-страницы.

#### Реализация
_request.py_
```python
import typing as tp
from urllib.parse import parse_qs, urlparse


class Request:
    def __init__(
            self,
            method: str,
            target: str,
            version: str,
            headers: tp.Dict[str, tp.Any]
    ):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers

    @property
    def path(self):
        return self._url.path

    @property
    def query(self):
        return parse_qs(self._url.query)

    @property
    def _url(self):
        return urlparse(self.target)
```

_response.py_
```python
import typing as tp


class Response:
    def __init__(
            self,
            status: int,
            reason: str,
            headers: tp.Optional[tp.Dict[str, tp.Any]] = None,
            body: tp.Optional[bytes] = None
    ):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```

_server.py_
```python
import email.message
import socket
import typing as tp
import json

from Lr1.task5.request import Request
from Lr1.task5.response import Response
from email.parser import Parser

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


class HTTPServer:
    def __init__(self, host: str, port: int):
        self.server: tp.Optional[socket.socket] = self.__create_tcp_socket(host, port)
        self._grades: tp.Dict[str, int] = {}

    def __create_tcp_socket(self, host: str, port: int) -> tp.Optional[socket.socket]:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((host, port))
            sock.listen()
            return sock
        except socket.error:
            sock.close()
            return None

    def __map_message_to_dict(self, message: email.message.Message) -> tp.Dict[str, tp.Any]:
        res_dict = {}
        for key in message.keys():
            res_dict[key] = message[key]

        return res_dict

    def __handle_post_grades(self, req: Request) -> Response:
        try:
            subject = req.query['subject'][0]
            grade = req.query['grade'][0]
            self._grades[subject] = int(grade)
        except Exception:
            raise HTTPError(400, "Bad Request")

        return Response(204, 'Created')

    def __handle_get_grades(self, req: Request) -> Response:
        accept = req.headers.get('Accept')

        if accept is None:
            raise HTTPError(400, "Bad Request")

        if 'application/json' in accept:
            content_type = 'application/json; charset=utf-8'
            body = json.dumps(self._grades)
        else:
            return Response(406, 'Not Acceptable')

        headers = {'Content-Type': content_type,
                   'Content-Length': len(body)}

        return Response(200, 'OK', headers, body.encode('utf-8'))

    def serve_forever(self):
        if self.server is None:
            return

        try:
            while True:
                conn, _ = self.server.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        except KeyboardInterrupt:
            self.server.close()

    def serve_client(self, conn: socket.socket):
        try:
            req = self.parse_request(conn)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except ConnectionResetError:
            conn = None
        except HTTPError as e:
            self.send_error(conn, e)

        if conn:
            conn.close()

    def parse_request(self, conn) -> Request:
        rfile = conn.makefile('rb')

        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)

        return Request(method, target, ver, headers)

    def parse_headers(self, rfile) -> tp.Dict[str, tp.Any]:
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise HTTPError(494, 'Request header too large')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')

        sheaders = b''.join(headers).decode('iso-8859-1')
        message = Parser().parsestr(sheaders)

        return self.__map_message_to_dict(message)

    def parse_request_line(self, rfile) -> tp.Tuple[str, ...]:
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request', 'Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()

        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')

        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')

        return method, target, ver

    def handle_request(self, req: Request) -> Response:
        if req.path == '/api' and req.method == 'POST':
            return self.__handle_post_grades(req)

        if req.path == '/api' and req.method == 'GET':
            return self.__handle_get_grades(req)

        raise HTTPError(404, 'Not found')

    def send_response(self, conn: socket.socket, resp: Response):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if resp.headers:
            for (key, value) in resp.headers.items():
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if resp.body:
            wfile.write(resp.body)

        wfile.flush()
        wfile.close()

    def send_error(self, conn: socket.socket, err: HTTPError):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except Exception:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'

        resp = Response(
            status,
            reason,
            {'Content-Length': len(body)},
            body
        )

        self.send_response(conn, resp)
```

#### Запуск
```python
host = "127.0.0.1"
port = 1234
serv = HTTPServer(host, port)

serv.serve_forever()
```