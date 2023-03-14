import json
import socket
from request import Request, Response
from email.parser import Parser

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self._name = name
        self._marks = {'Физкультура': 5}
        print(f"[RUNNING] Created HTTPServer '{name}'")

    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()
            print(f"[LISTENING] Server '{self._name}' on {self._host}:{self._port}\r\n")
            while True:
                conn, addr = serv_sock.accept()
                print(f"[NEW]: {addr}")
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('[ERROR]: Client serving failed', e)
        finally:
            print('[EXIT]')
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
        host = headers.get('Host')
        if not host:
            raise HTTPError(400, 'Bad request', 'Host header is missing')
        if host != f'{self._host}:{self._port}':
            raise HTTPError(404, 'Not found')
        return Request(method, target, ver, headers, rfile)

    @staticmethod
    def parse_request_line(rfile):
        raw = rfile.readline(MAX_LINE + 1)
        if len(raw) > MAX_LINE:
            raise HTTPError(400, 'Bad request', 'Request line is too long')
        req_line = str(raw, 'iso-8859-1')
        words = req_line.split()
        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')
        method, target, ver = words
        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')
        return method, target, ver

    @staticmethod
    def parse_headers(rfile):
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
        if req.path == '/update' and req.method == 'POST':
            return self.handle_post_mark(req)
        if req.path == '/marks' and req.method == 'GET':
            return self.handle_get_marks(req)
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
        resp = Response(status, reason, [('Content-Length', len(body))], body)
        self.send_response(conn, resp)

    def handle_post_mark(self, req):
        self._marks[req.query['name'][0]] = req.query['mark'][0]
        return Response(204, 'Created')

    def handle_get_marks(self, req):
        accept = req.headers.get('Accept')
        if 'text/html' in accept:
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<div>Оценки ({len(self._marks)})</div>'
            body += '<ul>'
            for m in self._marks:
                body += f'<li>{m}: {self._marks[m]}</li>'
            body += '</ul>'
            body += '</body></html>'
        elif 'application/json' in accept:
            contentType = 'application/json; charset=utf-8'
            body = json.dumps(self._marks)
        else:
            return Response(406, 'Not Acceptable')
        body = body.encode('utf-8')
        headers = [('Content-Type', contentType), ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)


class HTTPError(Exception):
    def __init__(self, status, reason, body=None):
        super()
        self.status = status
        self.reason = reason
        self.body = body


if __name__ == '__main__':
    print('[LOADING...]')
    host = socket.gethostbyname(socket.gethostname())
    port = 7777
    serv = MyHTTPServer(host, port, 'Marks')
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print('Exit!')
        pass
