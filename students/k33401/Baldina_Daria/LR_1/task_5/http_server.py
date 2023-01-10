import socket
from urllib.parse import parse_qs, urlparse
import json


class Request:
    def __init__(self, method, target, headers, version, data):
        self.method = method
        self.target = target
        self.version = version
        self.url = urlparse(self.target)
        self.query = parse_qs(self.url.query)
        self.path = self.url.path
        self.headers = headers
        self.data = data

class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.marks = {}
  
  def serve_forever(self):
    serv_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM, proto=0)

    try:
        serv_sock.bind((self.host, self.port))
        serv_sock.listen()
        while True:
            client, address = serv_sock.accept()
            self.serve_client(client)
    except KeyboardInterrupt:
        serv_sock.close()

    
  def serve_client(self, client):
    try:
        data = client.recv(1024).decode('utf-8')
        req = self.parse_request(data)
        res = self.handle_request(req)
        self.send_response(client, res)
    except Exception as e:
            print(e)
    client.close()

  def parse_request(self, data):
    req = data.rstrip('\r\n')
    words = req[:data.index("\n")].split()
    if len(words) != 3:                 # и ожидаем ровно 3 части
      raise Exception('Malformed request line')

    method, target, ver = words
    if ver != 'HTTP/1.1':
      raise Exception('Unexpected HTTP version')

    headers = self.parse_headers(req)
    return Request(method=method, target=target, version=ver, headers=headers, data=data)

  def parse_headers(self, req_line):
    headers = req_line[req_line.index('\n')+1:].split('\n')
    hdict={}
    for h in headers:
      k, v = h.split(':', 1)
      hdict[k] = v
    return hdict

  def handle_request(self, req):
        if req.path == '/marks' and req.method == 'GET':
            return self.handle_get_marks()

        if req.path == '/marks' and req.method == 'POST':
            return self.handle_post_marks(req)

  def handle_post_marks(self, req):
        discipline = req.query['discipline'][0]
        grade = req.query['grade'][0]

        if discipline not in self.marks:
            self.marks[discipline] = []

        self.marks[discipline].append(grade)

        return self.handle_get_marks()

  def handle_get_marks(self):
        content_type = 'text/html; charset=utf-8'
        body = '<html><head><style></style></head><body>'
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += """<form action="/form-request" method="post"><label>Дисциплина</label><input name="discipline" /><br><label>Оценка</label><input name="grade"/><input type="submit"></form>"""
        for subject in self.marks:
            body += f'<div><span>{subject}: {self.marks[subject]}</span></div>'
        body += """</tbody></table>"""
        body += '</body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)


  def send_response(self, client, res):
        rfile = client.makefile('wb')
        status_line = f'HTTP/1.1 {res.status} {res.reason}\r\n'
        rfile.write(status_line.encode('utf-8'))

        if res.headers:
            for (key, value) in res.headers:
                header_line = f'{key}: {value}\r\n'
                rfile.write(header_line.encode('utf-8'))

        rfile.write(b'\r\n')

        if res.body:
            rfile.write(res.body)

        rfile.flush()
        rfile.close()
    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.


if __name__ == '__main__':
  host = '127.0.0.1' 
  port = 8000
  serv = MyHTTPServer(host, port)
  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass