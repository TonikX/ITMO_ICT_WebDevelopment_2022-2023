##  Task 1
* `ServerSide.py`
```python
import socket
sock = socket.socket()
# if "127.0.0.1" - connect only my cp host, if "0.0.0.0"- connect all hosts
# 8080 - port
sock.bind(("", 8080))
# set listening and queue size
sock.listen(1)
# accept() return client socket and client address
# Адрес — массив, состоящий из IP-адреса и порта
conn, addr = sock.accept()
# get data
data = conn.recv(16384)
decodeData = data.decode("utf-8")
print("Server: " + decodeData)
# two ways for send data, in both ways data should be encoded
massage = "Hello, client"
# conn.send(b"Hello, client\n")
conn.send(massage.encode("utf-8"))
# close connection
conn.close()
```
* `ClientSide.py`
```python
import socket
sock = socket.socket()
# connect to port which is listening server
sock.connect(("127.0.0.1", 8080))
massage = "Hello, server"
sock.send(massage.encode("utf-8"))
data = sock.recv(16384)
decodeData = data.decode("utf-8")
print("Client: " + decodeData)
```

##  Task 2
* `ServerSide.py`
```python
import socket
import math
def math_square(m_data):
    split_str = m_data.split()
    if split_str[0] == "a":
        return int(split_str[1]) * int(split_str[2])
    elif split_str[0] == "b":
        return int(split_str[1]) * int(split_str[2]) * math.sin(math.radians(int(split_str[3])))
    elif split_str[0] == "c":
        return (1 / 2) * int(split_str[1]) * int(split_str[2]) * math.sin(math.radians(int(split_str[3])))
    else:
        return 0
sock = socket.socket()
sock.bind(("", 8080))
sock.listen(1)
conn, addr = sock.accept()
try:
    while 1:
        try:
            conn.settimeout(10)
            data = conn.recv(16384)
            if not data:
                break
            decoded_data = data.decode("utf-8")
            massage_out = str(math_square(decoded_data))
            conn.send(massage_out.encode("utf-8"))
        except socket.error:
            print("connection timed out")
            break
        finally:
            conn.close()
finally:
    sock.close()
```
* `ClientSide.py`
```python
import socket
sock = socket.socket()
sock.connect(("127.0.0.1", 8080))
massage = input("Which formula do you prefer?\na. S = a*h\nb. S = a*b*sin(a^b)\n"
                "c. S = 0.5*d1*d2+sin(d1^d2)\nInput latter and params: ")
sock.send(massage.encode("utf-8"))
sock.settimeout(1)
data = sock.recv(16384)
decodeData = data.decode("utf-8")
print("Answer: " + decodeData)
```

##  Task 3
* `ServerSide.py`
```python
import socket
import os
with socket.socket() as s:
    s.bind(('', 8080))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        work_path = os.getcwd()
        res_path = ('\\'.join(work_path.split('\\')[:-1]) + '\\res\\index.html').replace('\\', '/')
        with open(res_path) as fin:
            message = fin.read()
        print(conn.recv(16348).decode('utf-8'))
        response = 'HTTP/1.0 200 OK\n\n' + message
        conn.sendall(response.encode('utf-8'))
```
* `ClientSide.py`
```python
import socket
with socket.socket() as s:
    s.connect(('127.0.0.1', 8080))
    s.settimeout(5)
    s.send(b"GET / HTTP/1.1\n")
    data = s.recv(16384)
    decodeData = data.decode('utf-8')
    print(decodeData)
```

* `index.html`
```html
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Title</title>
  </head>
  <body>
    <h1>My first title</h1>
    <p>My first article</p>
  </body>
</html>
```

##  Task 4
* `ServerSide.py`
```python
import socket
import threading
def accept():
    while 1:
        try:
            conn, addr = s.accept()
            print(f"New user {conn.getpeername()[1]} was added")
            conn.send(b"...Write \"/exit\" for live this chat...\n")
            message = f"...New member: {addr[1]}...\n"
            for user in users:
                user.send(message.encode('utf-8'))
            users.append(conn)
            # Start a thread which receives messages
            t_in = threading.Thread(target=in_data, name='in', args=(conn,))
            t_in.start()
        except socket.error:
            break
def in_data(t_conn):
    t_user = t_conn.getpeername()[1]
    while 1:
        try:
            data = t_conn.recv(1024)
            decode_data = data.decode('utf-8')
            # Start a thread which sends messages
            t_out = threading.Thread(target=out_data, name='out', args=(t_conn, decode_data, ), daemon=True)
            t_out.start()
            t_out.join()
        except socket.error:
            print(f"User {t_user} left")
            break
def out_data(t_conn, message):
    t_user = t_conn.getpeername()[1]
    if message == '/exit':
        users.remove(t_conn)
        specific_message = f"...User {t_user} left...\n".encode('utf-8')
        t_conn.close()
    else:
        specific_message = f"User {t_user}: {message}".encode('utf-8')
    for user in users:
        if user == t_conn:
            continue
        user.send(specific_message)
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = ''
        port = 8080
        s.bind((host, port))
        s.listen(5)
        users = []
        print('Chat\'s started')
        # Start a thread which accepts sockets
        t_accept = threading.Thread(target=accept, name='accept', daemon=True)
        t_accept.start()
        while 1:
            # Checking server shutdown
            check = input('Write \"/terminate\" to stop this chat\n')
            if check == '/terminate':
                s.close()
                print('Chat\' stopped')
                break
```
* `User1.py`
```python
import socket
import threading
import time
def out_data():
    time.sleep(2)
    m = 'Hi, i\'m 0\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(5)
    m = 'What?\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(4)
    m = 'No, it\'s you!\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): No, {m}')
    time.sleep(5)
    s.send(b'/exit')
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 8080
        s.connect((host, port))
        t = threading.Thread(target=out_data, name='out', daemon=True)
        i = 1
        while 1:
            try:
                in_data = s.recv(1024)
                decodeData = in_data.decode("utf-8")
                if not in_data:
                    print('You left the chat')
                    break
                print(decodeData)
                if i:
                    print('You have joined the chat')
                    t.start()
                    i -= 1
            except socket.error:
                print('Server was terminated')
                break
```

* `User2.py`
```python
import socket
import threading
import time
def out_data():
    time.sleep(2)
    m = 'Hiii, i\'m 1\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    m = 'Sgsvd...\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(4)
    m = 'You loser?\n'
    s.send(m.encode('utf-8'))
    print(f'You ({s.getsockname()[1]}): {m}')
    time.sleep(5)
    s.send(b'/exit')
if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = '127.0.0.1'
        port = 8080
        s.connect((host, port))
        t = threading.Thread(target=out_data, name='out', daemon=True)
        i = 1
        while 1:
            try:
                in_data = s.recv(1024)
                decodeData = in_data.decode("utf-8")
                if not in_data:
                    print('You left the chat')
                    break
                print(decodeData)
                if i:
                    print('You have joined the chat')
                    t.start()
                    i -= 1
            except socket.error:
                print('Server was terminated')
                break
```

##  Task 5
* `MyHTTPServer.py`
```python
import os
import socket
from email.parser import Parser
from HTTPError import HTTPError
from Response import Response
from Request import Request
MAX_HEADERS = 100
class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._subjects = {}
    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen(1)
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
            # Parse request and return Request(method, target, ver, headers, rfile)
            req = self.parse_request(conn)
            # Return Response(200, 'OK', headers, body)
            resp = self.handle_request(req)
            self.send_response(conn, resp)
        except Exception as e:
            self.send_error(conn, e)
        if conn:
            req.rfile.close()
            conn.close()
    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
        headers = self.parse_headers(rfile)
        return Request(method, target, ver, headers, rfile)
    def parse_request_line(self, rfile):
        raw = rfile.readline()
        req_line = str(raw, 'utf-8')
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request', )
        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver
    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline()
            if line in (b'\r\n', b'\n', b''):
                break
            headers.append(line)
            if len(headers) > MAX_HEADERS:
                raise HTTPError(494, 'Too many headers')
        sheaders = b''.join(headers).decode('utf-8')
        return Parser().parsestr(sheaders)
    def parse_values(self, req_values):
        param = req_values.decode('utf-8').split('&')
        subject = param[0][len('subject='):]
        grade = param[1][len('grade='):]
        if not subject or not grade:
            raise HTTPError(400, 'Bad request', 'Params missing')
        return subject, grade
    def handle_request(self, req):
        if req.target == '/welcome' and req.method == 'GET':
            return self.handle_get_welcome()
        if req.method == 'POST':
            return self.handle_post_subjects(req)
        if req.target.startswith('/subjects') and req.method == 'GET':
            return self.handle_get_subjects()
        raise HTTPError(404, 'Not found')
    def send_response(self, conn, resp):
        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        wfile.write(status_line.encode('utf-8'))
        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('utf-8'))
        wfile.write(b'\r\n')
        if resp.body:
            wfile.write(resp.body)
        wfile.flush()
        wfile.close()
    def send_error(self, conn, err):
        try:
            status = err.status
            reason = err.reason
            body = (err.body or err.reason).encode('utf-8')
        except Exception:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'
        resp = Response(status, reason, [('Content-Length', len(body))], body)
        self.send_response(conn, resp)
    def handle_get_welcome(self):
        content_type = 'text/html; charset=utf-8'
        work_path = os.getcwd()
        res_path = ('\\'.join(work_path.split('\\')[:-1]) + '\\res\\welcome.html').replace('\\', '/')
        with open(res_path) as fin:
            body = fin.read()
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)
    def handle_post_subjects(self, req):
        req_values = req.rfile.readline()
        subject, grade = self.parse_values(req_values)
        subject_id = len(self._subjects) + 1
        self._subjects[subject_id] = {'id': subject_id, 'subject': subject, 'grade': grade}
        return Response(204, 'Created')
    def handle_get_subjects(self):
        content_type = 'text/html; charset=utf-8'
        body = '<html><head></head><body>'
        body += f'<div>Count of subjects: {len(self._subjects)}</div>'
        body += '<ul>'
        for u in self._subjects.values():
            body += f'<li>{u["subject"]}, {u["grade"]}</li>'
        body += '</ul>'
        body += '</body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type), ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)
if __name__ == '__main__':
    s_host = ''
    s_port = 8080
    serv = MyHTTPServer(s_host, s_port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
```

* `HTTPError.py`
```python
class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body
```

* `Response.py`
```python
class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body
```

* `Request.py`
```python
class Request:
    def __init__(self, method, target, version, headers, rfile):
        self.method = method
        self.target = target
        self.version = version
        self.headers = headers
        self.rfile = rfile
    def body(self):
        size = self.headers.get('Content-Length')
        if not size:
            return None
        return self.rfile.read(size)
```

* `welcome.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta content="text/html" charset="UTF-8">
    <title>List of subjects</title>
</head>
<body>
    <h1>List of subjects</h1>

    <form action="" method="POST">
        <p>Write a subject:</p>
        <input type="text" name="subject" id="subject" placeholder="Math">

        <p>Write a grade:</p>
        <input type="text" name="grade" id="grade" placeholder="1-5"><br>
        <br>
        <button type="submit" name="add_subject" id=add_subject">Add subject</button>
    </form>
    <br>
    <form action="/subjects" method="GET">
        <button type="submit" name="see_subjects" id="see_subjects">See subjects</button>
    </form>
</body>
</html>
```