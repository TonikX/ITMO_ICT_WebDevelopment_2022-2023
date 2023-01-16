# Лабораторная работа №1

## Задача №1

* `_config.py`

```python
SOCKET_ADDR = '127.0.0.1'
SOCKET_PORT = 8080
SOCKET_BUFF_SIZE = 1024
```

* `server.py`

```python
import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))

    print("UDP server up and listening")
    while True:
        message, addr = conn.recvfrom(SOCKET_BUFF_SIZE)

        print(f"Message from client: {message.decode('utf-8')}")
        print(f"Client address: {addr}")

        conn.sendto(b'Hello, client', addr)
        break
```

* `client.py`

```python
import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    conn.connect((SOCKET_ADDR, SOCKET_PORT))

    conn.send(b'Hello, server!')

    message = conn.recv(SOCKET_BUFF_SIZE)
    print(f"Message from server: {message.decode('utf-8')}")
```

## Задача №2

* `_config.py`

```python
SOCKET_ADDR = '127.0.0.1'
SOCKET_PORT = 8080
SOCKET_BUFF_SIZE = 1024
```

* `server.py`

```python
import socket

from _config import *


def parse_params(params):
    return list(map(int, params.split(' ')))


def solve_pythagorean(a, b):
    return (a ** 2 + b ** 2) ** 0.5


if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))
    conn.listen(10)

    print("TCP server up and listening")
    while True:
        try:
            client_socket, addr = conn.accept()
            message = client_socket.recv(SOCKET_BUFF_SIZE)

            params = message.decode('utf-8')
            print(f"Message from client: {params}")
            print(f"Client address: {addr}")

            a, b = parse_params(params)
            result = str(solve_pythagorean(a, b))

            client_socket.send(result.encode('utf-8'))
        except:
            break
    conn.close()
```

* `client.py`

```python
import socket

from _config import *

if __name__ == '__main__':
    print('Solving Pythagorean theorem')
    params = input('Enter a, b [space-separated]: ')
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((SOCKET_ADDR, SOCKET_PORT))

    conn.send(params.encode('utf-8'))

    message, server = conn.recvfrom(SOCKET_BUFF_SIZE)
    print(f"Message from server: {message.decode('utf-8')}")

    conn.close()
```

## Задача №3

* `_config.py`

```python
SOCKET_ADDR = '127.0.0.1'
SOCKET_PORT = 8080
SOCKET_BUFF_SIZE = 1024
```

* `server.py`

```python
import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.bind((SOCKET_ADDR, SOCKET_PORT))
    conn.listen(10)

    with open('index.html', 'r') as f:
        body = f.read()
    response_type = 'HTTP/1.0 200 OK\n'
    headers = 'Content-Type: text/html\n\n'

    response = response_type + headers + body

    print("HTTP server up and listening")
    while True:
        try:
            client_socket, addr = conn.accept()
            message = client_socket.recv(SOCKET_BUFF_SIZE)
            client_socket.send(response.encode('utf-8'))
            client_socket.close()
        except:
            break
    conn.close()
```

* `client.py`

```python
import socket

from _config import *

if __name__ == '__main__':
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conn.connect((SOCKET_ADDR, SOCKET_PORT))

    conn.send('GET /index.html HTTP/1.0'.encode('utf-8'))

    message, server = conn.recvfrom(SOCKET_BUFF_SIZE)
    print(f"Message from server: {message.decode('utf-8')}")

    conn.close()
```

* `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Hello world!</title>
</head>
<body>
Hello world!
</body>
</html>
```

## Задача №4

* `_config.py`

```python
import logging

SOCKET_ADDR = '127.0.0.1'
SOCKET_PORT = 8080
SOCKET_BUFF_SIZE = 16400

LOGGING_LEVEL = logging.INFO


class SYSTEM_CODES:
    ADD_USER_TO_ROOM = 1
    REMOVE_USER_FROM_ROOM = 2
```

* `server.py`

```python
import json
import socket
import threading

from _config import *


class ChatServer:
    class Room:
        def __init__(self, name):
            self.name = name
            self.members = {}

        def send_message(self, user_from, message):
            disconnected_members = []
            for username in self.members:
                try:
                    self.members[username].send(json.dumps({
                        'message': message,
                        'from':    user_from
                    }).encode('utf-8'))
                except BrokenPipeError:
                    disconnected_members.append(username)
            for username in disconnected_members:
                self.remove_member(username)

        def add_member(self, user, client_socket):
            self.members[user] = client_socket
            self.send_message(
                'system',
                f'User "{user}" has joined the room'
            )
            return len(self.members)

        def remove_member(self, user):
            del self.members[user]
            self.send_message(
                'system',
                f'User "{user}" has left the room'
            )
            return len(self.members)

    def __init__(self):
        self.rooms = {}
        logging.debug("Starting server")
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((SOCKET_ADDR, SOCKET_PORT))
        self.socket.listen(100)
        logging.info("TCP server up and listening")

    def process_received_message(self, data_raw, client_socket):
        data = json.loads(data_raw)

        room_name = data.get('room')
        user_from = data.get('from')
        message = data.get('message')
        system_code = data.get('system')

        if room_name not in self.rooms:
            self.rooms[room_name] = self.Room(
                room_name
            )
        room = self.rooms[room_name]

        if message is None:
            if system_code == SYSTEM_CODES.ADD_USER_TO_ROOM:
                room.add_member(
                    user_from,
                    client_socket
                )
            elif system_code == SYSTEM_CODES.REMOVE_USER_FROM_ROOM:
                members_left = room.remove_member(
                    user_from
                )
                if members_left == 0:
                    del self.rooms[room_name]
        else:
            room.send_message(user_from, message)
            logging.debug(self.rooms)

    def client_thread(self, client_socket):
        while True:
            try:
                data_raw = client_socket.recv(SOCKET_BUFF_SIZE)
                if data_raw != b'':
                    logging.debug(data_raw)
                    self.process_received_message(data_raw, client_socket)
            except Exception as e:
                logging.error(e)
                break

    def listen(self):
        while True:
            try:
                client_socket, addr = self.socket.accept()
                logging.debug(addr)

                client_thread = threading.Thread(
                    target=self.client_thread,
                    args=(client_socket,)
                )
                client_thread.start()

            except Exception as e:
                logging.error(e)
                self.socket.close()
                break


if __name__ == '__main__':
    logformat = "%(asctime)s – %(message)s"
    logging.basicConfig(
        format=logformat,
        level=LOGGING_LEVEL,
        datefmt="%H:%M:%S"
    )
    server = ChatServer()
    server.listen()
```

* `client.py`

```python
import json
import signal
import socket
import threading

from _config import *


class ChatClient:
    def __init__(self, username):
        self.shutdown_from_thread = False
        self.shutdown = threading.Event()
        self.thread_sending = None
        self.thread_receiving = None
        self.room = None
        self.username = username
        logging.debug('Connecting to server')
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((SOCKET_ADDR, SOCKET_PORT))
        logging.debug('Connected successfully')

    def select_room(self):
        self.leave_room()
        self.room = input('Enter chat room name (leave blank to exit): ')
        if self.room == '':
            self.graceful_shutdown()
        print(f'Chat room "{self.room}" selected\n'
              f'To change room enter "exit-room" in message box\n'
              f'To send message enter text and hit "Enter"')
        self.socket.send(
            json.dumps({
                'message': None,
                'system':  SYSTEM_CODES.ADD_USER_TO_ROOM,
                'from':    self.username,
                'room':    self.room
            }).encode('utf-8')
        )

    def leave_room(self):
        if self.room is not None:
            self.socket.send(
                json.dumps({
                    'message': None,
                    'system':  SYSTEM_CODES.REMOVE_USER_FROM_ROOM,
                    'from':    self.username,
                    'room':    self.room
                }).encode('utf-8')
            )

    def graceful_shutdown(self, *args):
        self.leave_room()
        self.socket.close()
        self.shutdown.set()
        if not self.shutdown_from_thread:
            logging.info('Press enter to shutdown')
            self.thread_sending.join()
            self.thread_receiving.join()

    def listen(self):
        if self.room is None:
            self.select_room()
        self.thread_sending = threading.Thread(
            target=self.serve_sending
        )
        self.thread_receiving = threading.Thread(
            target=self.serve_receiving
        )
        self.thread_receiving.start()
        self.thread_sending.start()

    def serve_receiving(self):
        while not self.shutdown.is_set():
            try:
                data_raw = self.socket.recv(SOCKET_BUFF_SIZE)
                if data_raw != b'':
                    data = json.loads(data_raw)
                    print(f"{data.get('from')}: {data.get('message')}")
                    logging.debug(data_raw.decode('utf-8'))
            except Exception as e:
                logging.error(e)
                break

    def serve_sending(self):
        while not self.shutdown.is_set():
            try:
                message = input()
                if message == 'exit-room':
                    self.select_room()
                elif message == 'exit':
                    self.shutdown_from_thread = True
                    self.graceful_shutdown()
                else:
                    self.socket.send(
                        json.dumps({
                            'message': message,
                            'from':    self.username,
                            'room':    self.room
                        }).encode('utf-8')
                    )
                    logging.debug('sent message')
            except Exception as e:
                logging.error(e)
                break


if __name__ == '__main__':
    logformat = "%(asctime)s – %(message)s"
    logging.basicConfig(
        format=logformat,
        level=LOGGING_LEVEL,
        datefmt="%H:%M:%S"
    )

    username = input('Enter username: ')
    client = ChatClient(username)

    signal.signal(signal.SIGINT, client.graceful_shutdown)
    signal.signal(signal.SIGTERM, client.graceful_shutdown)

    client.listen()
```