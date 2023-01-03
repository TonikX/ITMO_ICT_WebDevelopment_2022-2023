import socket
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

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
    size = int(self.headers.get('Content-Length'))
    body = self.rfile.readline(size)
    args = str(body, 'iso-8859-1')
    return parse_qs(args)

  @property
  @lru_cache(maxsize=None)
  def url(self):
    return urlparse(self.target)


class Response:
  def __init__(self, status, reason, headers=None, body=None):
    self.status = status
    self.reason = reason
    self.headers = headers
    self.body = body

MAX_LINE = 64 * 1024

class MyHTTPServer:
  def __init__(self, host, port, server_name):
    self._host = host
    self._port = port
    self._server_name = server_name
    self._grades = {}
  
  def serve_forever(self):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((self._host, self._port))
    server.listen()
    while True:
        client, _ = server.accept()
        self.serve_client(client)

  def serve_client(self, client):
    req = self.parse_request(client)
    resp = self.handle_request(req)
    self.send_response(client, resp)

  def parse_request(self, client):
    rfile = client.makefile('rb')
    raw = rfile.readline(MAX_LINE + 1)
    req_line = str(raw, 'iso-8859-1')
    req_line = req_line.rstrip('\r\n')
    words = req_line.split() 
    method, target, ver = words   
    headers = self.parse_headers(rfile)
    return Request(method, target, ver, headers, rfile)

  def parse_headers(self, rfile):
    headers = []
    while True:
        line = rfile.readline(MAX_LINE + 1)
        if line in (b'\r\n', b'\n', b''):
            break
        headers.append(line)
    sheaders = b''.join(headers).decode('iso-8859-1')
    return Parser().parsestr(sheaders)


  def handle_request(self, req):
    if req.path == '/' and req.method == 'POST':
      grade_id = len(self._grades) + 1
      self._grades[grade_id] = {'id': grade_id, 'course': req.query['course'][0], 'grade': req.query['grade'][0]}
      return self.update_register()

    if req.path.startswith('/') and req.method == 'GET':
      return self.update_register()

  def update_register(self):
    courses = []
    for n in range(1, len(self._grades)+1):
      if self._grades[n]['course'] not in courses:
        courses.append(self._grades[n]['course'])
    course_grades = {}
    for c in courses:
      course_grades[c] = []
      for n in range(1, len(self._grades)+1):
        if self._grades[n]['course'] == c:
          course_grades[c].append(self._grades[n]['grade'])
    contentType = 'text/html; charset=utf-8'
    body = '<!DOCTYPE html><head></head><body>'
    for c in courses:
      body += f"{c}: {', '.join(map(str, course_grades[c]))}<br>"
    body += '<br><br>'
    body += '<form method="post">'
    body += 'Дисциплина: <br><input type="text" id="course" name="course"><br>'
    body += 'Оценка: <br><input type="text" id="grade" name="grade"> <br><br>'
    body += '<input type="submit" value="Отправить">'
    body += '</form></body></html>'
    body += '</body></html>'
    body = body.encode('utf-8')
    headers = [('Content-Type', contentType),
              ('Content-Length', len(body))]
    return Response(200, 'OK', headers, body)

  def send_response(self, client, resp):
    wfile = client.makefile('wb')
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


if __name__ == '__main__':
  MyHTTPServer("127.0.0.1", 9101, 'myserver.com').serve_forever()