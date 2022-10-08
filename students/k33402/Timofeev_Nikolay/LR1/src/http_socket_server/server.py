import socket
import sys
from email.parser import Parser
from functools import lru_cache
from urllib.parse import parse_qs, urlparse

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    def __init__(self, host: str, port: int, server_name: str):
        self._host = host
        self._port = port
        self._server_name = server_name
        self._data: dict[str, list[str]] = {}

    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                clientsocket, _ = serv_sock.accept()
                try:
                    self.serve_client(clientsocket)
                except Exception as e:
                    print('Client serving failed:', e)
        finally:
            serv_sock.close()

    def serve_client(self, clientsocket):
        try:
            req = self.parse_request(clientsocket)
            resp = self.handle_request(req)
            self.send_response(clientsocket, resp)
        except ConnectionResetError:
            clientsocket = None
        except Exception as e:
            print('Client serving failed:', e)

        if clientsocket:
            clientsocket.close()

    def parse_request(self, clientsocket):
        rfile = clientsocket.makefile('rb')
        raw = rfile.readline(MAX_LINE + 1)

        if len(raw) > MAX_LINE:
            raise Exception('Request line is too long')

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()
        if len(words) != 3:
            raise Exception('Malformed request line')

        method, target, ver = words

        if ver != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        headers = self.parse_headers(rfile)
        host = headers.get('Host')
        if not host:
            raise Exception('Bad request')
        if host not in (self._server_name, f'{self._server_name}:{self._port}'):
            raise Exception('Not found')

        return Request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)
            if len(line) > MAX_LINE:
                raise Exception('Header line is too long')

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)
            if len(headers) > MAX_LINE:
                raise Exception('Too many headers')
        sheaders = b''.join(headers).decode('iso-8859-1')

        return Parser().parsestr(sheaders)

    def handle_request(self, req):
        if req.path == '/rating' and req.method == 'POST':
            return self.handle_post_grades(req)

        if req.path.startswith('/rating/') and req.method == 'GET':
            subject_name = req.path[len('/rating/'):]
            return self.handle_get_rating(req, subject_name)

        raise Exception('Request not found')

    def handle_post_grades(self, req):
        subject_name = req.query['subject_name'][0]
        grade = req.query['grade'][0]
        if subject_name in self._data.keys():
            self._data[subject_name].append(grade)
        else:
            new_subject = []
            new_subject.append(grade)
            self._data[subject_name] = new_subject

        return Response(204, 'Created')

    def handle_get_rating(self, req, subject_name):
        if subject_name not in self._data.keys():
            raise Exception('Request not found')

        content_type = 'text/html; charset=utf-8'
        body = '<html><head></head><body>'
        ans = f'{subject_name}: '

        for grade in self._data[subject_name]:
            ans += grade + ' '

        body += f'<div>{ans}</div>'
        body += '</body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type), ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def send_response(self, clientsocket, response):
        wfile = clientsocket.makefile('wb')
        status_line = f'HTTP/1.1 {response.status} {response.reason}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if response.headers:
            for (key, value) in response.headers:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if response.body:
            wfile.write(response.body)

        wfile.flush()
        wfile.close()


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


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


if __name__ == '__main__':
    host = "0.0.0.0"
    port = 8888
    name = "index.html"
    server = MyHTTPServer(host, port, name)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
