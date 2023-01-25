# Лабораторная работа №1

## Задача №1

`server.py`

```python
import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
conn, addr = sock.accept()

data = conn.recv(1024)
print(data.decode('utf-8'))

msg = 'Hello, client!'
conn.send(msg.encode('utf-8'))

conn.close()
```

`client.py`

```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

msg = 'Hello, server!'
sock.send(msg.encode('utf-8'))

data = sock.recv(1024)
sock.close()

print(data.decode('utf-8'))
```

## Задача №2

`server.py`

```python
import socket

# d - площадь параллелограмма


class Server:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def parallelogram_square(self, base, height):
        return int(base) * int(height)

    def send(self, msg):
        self.conn.send(msg.encode('utf-8'))

    def receive(self):
        data = self.conn.recv(1024)
        return data.decode('utf-8')

    def start(self):
        self.sock.bind(('', 9090))
        self.sock.listen(1)
        self.conn, self.addr = self.sock.accept()

    def close(self):
        self.sock.close()


def main():
    srv = Server()
    srv.start()

    srv.send("Input base lenght of the parallelogram: ")
    base = srv.receive()

    srv.send("Input height of the parallelogram: ")
    height = srv.receive()

    square = srv.parallelogram_square(base, height)
    srv.send(f"Square of the parallelogram is {square}")

    srv.close()


if __name__ == '__main__':
    main()
```

`client.py`

```python
import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

data = sock.recv(1024).decode('utf-8')
print(data)
base = input('>>')
sock.send(base.encode('utf-8'))

data = sock.recv(1024).decode('utf-8')
print(data)
height = input('>>')
sock.send(height.encode('utf-8'))

data = sock.recv(1024).decode('utf-8')
print(data)

input('Push ENTER to exit >>')
```

## Задача №3

`server.py`

```python
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9090))
    sock.listen(1)

    while True:
        try:
            conn, addr = sock.accept()

            response_type = "HTTP/1.0 200 OK\n"
            headers = "Content-Type: text/html\n\n"

            with open('index.html', 'r') as f:
                body = f.read()

            res = response_type + headers + body

            conn.send(res.encode('utf-8'))
            conn.close()
        except KeyboardInterrupt:
            sock.close()
            break


if __name__ == "__main__":
    main()
```

`index.html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>wtf...</title>
    <style type="text/css">
      body {
        background-image: url('https://www.meme-arsenal.com/memes/d9376e8a26b220ed9cc58f90327353f6.jpg');
        background-repeat: no-repeat;
        background-size: cover;
        color: white;
        word-break: break-all;
      }
    </style>
  </head>
  <body>
    <h1>AHAHAHAHAHHAAHAHAHAH</h1>
  </body>
</html>
```

## Задача №4

`server.py`

```python
import socket
import sys
from threading import Thread


class ChatServer:

    def __init__(self, host, port):
        self.clients = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __shutdown(self):
        for conn in self.clients:
            conn.close()
        self.sock.close()
        sys.exit(0)

    def __client_broadcast(self, message, sender):
        for conn in self.clients.copy():
            if conn != sender:
                try:
                    conn.send(message)
                except OSError:
                    print("Someone disconnected")
                    self.clients.remove(conn)

    def __client_listen(self, conn):
        conn.settimeout(30)
        while True:
            try:
                message = conn.recv(1024)
                print(message.decode())
                self.__client_broadcast(message, conn)
            except OSError:
                conn.close()
                break

    def __main(self):
        self.sock.bind((self.host, self.port))
        self.sock.listen(10)
        while True:
            try:
                conn, address = self.sock.accept()
                print(f"Connection at {address}")
                self.clients.append(conn)
                Thread(target=self.__client_listen, args=(conn,)).start()
            except KeyboardInterrupt:
                self.__shutdown()

    def run(self):
        Thread(target=self.__main).start()


if __name__ == '__main__':
    print("Starting server...")
    server = ChatServer('127.0.0.1', 14900)
    server.run()
    print("Server started")

```

`client.py`

```python
import socket
import sys
from threading import Thread


class ChatClient:
    def __init__(self, host, port, username):
        self.host = host
        self.port = port
        self.username = username
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __send(self):
        while True:
            try:
                msg = input('>>')
                if msg:
                    self.sock.send(f"{self.username}: {msg}".encode())
            except (KeyboardInterrupt, EOFError):
                self.conn.close()
                sys.exit(0)

    def __recieve(self):
        while True:
            try:
                msg = self.sock.recv(1024).decode()
                if msg:
                    print(msg)
            except KeyboardInterrupt:
                self.sock.close()
                sys.exit(0)
            except ConnectionError:
                # Unexpected connection error
                print("Connection error")
                self.sock.close()
                sys.exit(1)

    def run(self):
        # Connect
        self.sock.connect((self.host, self.port))
        # Run threaded functions
        Thread(target=self.__send).start()
        Thread(target=self.__recieve).start()


if __name__ == '__main__':
    name = input("Your username: ")
    print("Connecting to server...")
    client = ChatClient('127.0.0.1', 14900, name)
    client.run()

```

## Задача №5

`http_server_task_5.py`

```python
import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._marks = dict()

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
        try:
            method, url, headers = self.parse_request(conn)
            resp = self.handle_request(method, url)
            self.send_response(conn, resp, headers)
        except ConnectionResetError:
            conn = None

        if conn:
            conn.close()

    def parse_request(self, conn):
        if conn:
            data = conn.recv(16384).decode(
                'utf-8').replace('\r', '').split('\n')
            method, url, _ = data[0].split()
            headers = data[1: data.index('')]
            return method, url, headers

    def get_params(self, url):
        if '?' in url:
            i = url.index('?')
            params = {param.split('=')[0]: param.split('=')[1]
                      for param in url[i+1:].split('&') if param}
            url = url[:i].split('/')[1:]
        else:
            url = url.split('/')[1:]
            params = None
        return url, params

    def handle_request(self, method, url):
        url, params = self.get_params(url)
        print('-------------------------')
        print(url, params)
        if method == 'GET':
            resp = "HTTP/1.1 200 OK\n\n"
            body = '<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title></head></html><body>'
            if url[0] == 'marks':
                if len(url) == 1:
                    for subj in self._marks:
                        body += f"<b>{subj}</b> : {self._marks[subj]}</br></body></html>"
                elif len(url) == 2:
                    if url[1] in self._marks:
                        body += f"<b>{url[1]}</b> : {self._marks[url[1]]}</body></html>"
                    else:
                        body += '<h1>404 ERROR</h1></body></html>'
            else:
                body += '<h1>Wrong address</h1></body></html>'
            return resp + body

        elif method == 'POST':
            resp = "HTTP/1.1 201 Created\n\n"
            if url[0] == 'marks' and params:
                if 'subject' in params and 'mark' in params:
                    self._marks[params['subject']] = params['mark']
            return resp

    def send_response(self, conn, resp, headers):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9090

    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```
