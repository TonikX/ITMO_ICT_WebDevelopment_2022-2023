# Lab 1

## Task 1

* client.py

```python
import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello server')

msg = s.recv(1024)
print(msg.decode("utf-8"))
```

* server.py
```python
import socket
HOST = '127.0.0.1'
PORT = 14900
s = socket.socket()
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    cliensocket.send(b'Hello cleint')
    msg = cliensocket.recv(1024)
    if not msg:
        break
    print(msg.decode("utf-8"))
    cliensocket.close()
```

## Task 2

* client.py
```python
import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

m = ''
while not m.isdigit():
    m = input("Enter m of trapezoid: ")

h = ''
while not h.isdigit():
    h = input("Enter h of trapezoid: ")

#s.send(b'Hello server')
s.send(m.encode())
s.send(h.encode())
res = s.recv(1024)
print(res.decode("utf-8"))
```
* server.py
```python
import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    m = float(cliensocket.recv(1024).decode())
    if not m:
        break
    #print(m)
    h = float(cliensocket.recv(1024).decode())
    if not h:
        break    
    #print(h)
    res = m*h
    res = str(res)
    cliensocket.send(res.encode())

cliensocket.close()
```

## Task 3

* client.py
```python
import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

full_msg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <=0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
```
* server.py
```python

import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    html_file = open('index.html', 'r').read()
    cliensocket.sendall(f'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{html_file}'.encode())
    cliensocket.close()
```

## Task 4

* client.py
```python
import socket
import threading

HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

name = input("Enter your name: ")


def receive():
    while True:
        res = s.recv(1024)
        print(res.decode("utf-8"))

def write():
    while True:
        mes = input('')
        s.send(f"{name}: {mes}".encode("utf-8"))
    

thread = threading.Thread(target=write)
thread2 = threading.Thread(target=receive)
thread2.start() , thread.start()
```

* server.py
```python
import socket
import threading
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

clients = []

def brodcast(message):
    print(message)
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            brodcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            break

def receive():
    while True:
        client, address = s.accept()
        print("Connected with {}".format(str(address)))
        clients.append(client)
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
```

## Task 5

* MyHTTPServer.py
```python


import json
import socket
import sys
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64*1024
MAX_HEADERS = 100

class MyHTTPServer:
  def __init__(self, host, port, server_name):
    self._host = host
    self._port = port
    self._server_name = server_name
    self.marks = {}

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
      req = self.parse_request(conn)
      resp = self.handle_request(req)
      self.send_response(conn, resp)
    except ConnectionResetError:
      conn = None
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
    raw = rfile.readline(MAX_LINE + 1)
    if len(raw) > MAX_LINE:
      raise HTTPError(400, 'Bad request',
        'Request line is too long')

    req_line = str(raw, 'iso-8859-1')
    words = req_line.split()
    if len(words) != 3:
      raise HTTPError(400, 'Bad request',
        'Malformed request line')

    method, target, ver = words
    if ver != 'HTTP/1.1':
      raise HTTPError(505, 'HTTP Version Not Supported')
    return method, target, ver

  def parse_headers(self, rfile):
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
    return Parser().parsestr(sheaders)

  def handle_request(self, req):
    if req.path == '/marks' and req.method == 'POST':
      return self.handle_post_marks(req)

    if req.path == '/marks' and req.method == 'GET':
      return self.handle_get_marks(req)

    if req.path.startswith('/mark/'):
      subject_id = req.path[len('/mark/'):]
      print(subject_id)
      print('')
      if subject_id.isdigit():
        return self.handle_get_user(req, subject_id)

    raise HTTPError(404, 'Not found')

  def send_response(self, conn, resp):
    wfile = conn.makefile('wb')
    status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
    wfile.write(status_line.encode('iso-8859-1'))

    if resp.headers:
      for (key, value) in resp.headers:
        header_line = f'{key}: {value}\r\n'
        wfile.write(header_line.encode('iso-8859-1'))

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
    except:
      status = 500
      reason = b'Internal Server Error'
      body = b'Internal Server Error'
    resp = Response(status, reason,
                   [('Content-Length', len(body))],
                   body)
    self.send_response(conn, resp)

  def handle_post_marks(self, req):
    mark = int(req.query['mark'][0])
    if  mark < 1 or mark > 5:
        return Response(401, 'Value of mark have to be between 1 and 5')
    subject_id = len(self.marks) + 1
    self.marks[subject_id] = {'id': subject_id,
                            'name': req.query['name'][0],
                            'mark': req.query['mark'][0]}
                    
    return Response(204, 'Created')

  def handle_get_marks(self, req):
    accept = req.headers.get('Accept')
    if 'text/html' in accept:
      contentType = 'text/html; charset=utf-8'
      body = '<html><head></head><body>'
      body += f'<div>Marks ({len(self.marks)})</div>'
      body += '<ul>'
      for m in self.marks.values():
        body += f'<li>#{m["id"]} {m["name"]}, {m["mark"]}</li>'
      body += '</ul>'
      body += '</body></html>'

    elif 'application/json' in accept:
      contentType = 'application/json; charset=utf-8'
      body = json.dumps(self.marks)

    else:
      # https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/406
      return Response(406, 'Not Acceptable')

    body = body.encode('utf-8')
    headers = [('Content-Type', contentType),
               ('Content-Length', len(body))]
    return Response(200, 'OK', headers, body)


class Request:
  def __init__(self, method, target, version, headers, rfile):
    self.method = method
    self.target = target
    self.version = version
    self.headers = headers
    self.rfile = rfile

  @property
  def path(self):
    return self.url.path

  @property
  @lru_cache(maxsize=None)
  def query(self):
    return parse_qs(self.url.query)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)

  def body(self):
    size = self.headers.get('Content-Length')
    if not size:
      return None
    return self.rfile.read(size)

class Response:
  def __init__(self, status, reason, headers=None, body=None):
    self.status = status
    self.reason = reason
    self.headers = headers
    self.body = body

class HTTPError(Exception):
  def __init__(self, status, reason, body=None):
    super()
    self.status = status
    self.reason = reason
    self.body = body


if __name__ == '__main__':
  host = sys.argv[1]
  port = int(sys.argv[2])
  name = sys.argv[3]

  serv = MyHTTPServer(host, port, name)
  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass
```