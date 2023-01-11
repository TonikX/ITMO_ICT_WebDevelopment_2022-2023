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
        elif "text/htm" in accept:
            content_type = "text/html; charset=utf-8"
            body = '<html><head></head><body>'
            body += '<ul>'
            for subject in self._grades.keys():
                body += f'<li>{subject}: {self._grades[subject]}</li>'
            body += '</ul>'
            body += '</body></html>'
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
        print(method, target, ver, headers)
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


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 1234
    serv = HTTPServer(host, port)

    serv.serve_forever()
