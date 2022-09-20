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
        if req.path == '/welcome' and req.method == 'GET':
            return self.handle_get_welcome()

        if req.method == 'POST':
            return self.handle_post_subjects(req)

        if req.path == '/subjects' and req.method == 'GET':
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
