from Request import Request
from Response import Response
from HTTPError import HTTPError
from HTTPMethods import HTTPMethods
from email.parser import Parser as HeadersParser
from email.message import Message
from typing import Dict, List, Any

import json
import sys
import Configs

sys.path.append('..')
from Base.AsyncTCPServer import *


class HTTPServer(AsyncTCPServer):
    class Constants:
        assessments_path = "/assessments/"

    assessments: Dict[str, int] = {}
    clients: [socket_module.socket] = []

    def save_client(self, client_socket: socket_module.socket):
        self.clients.append(client_socket)

    def get_client_sockets(self) -> [socket_module.socket]:
        return self.clients

    def remove_client(self):
        self.clients = [
            client_socket
            for client_socket
            in self.get_client_sockets()
            if client_socket.getblocking() == False
        ]

    def handle_message(self, message: str, client_socket_address: SocketAddress):
        client_socket = next(x for x in self.get_client_sockets() if x.getpeername() == client_socket_address)

        try:
            request = self.parse_request_message(request_message=message)
            response = self.handle_request(request=request)

            self.send_response(response=response, client_socket=client_socket)
        except ConnectionResetError:
            self.remove_client()

            client_socket.close()
        except Exception:
            error = HTTPError(status=500, reason="Internal server error", body="Sorry")

            self.send_error(error=error, client_socket=client_socket)

    def parse_request_message(self, request_message: str) -> Request:
        request_lines = request_message.splitlines()

        method, target, version = self.parse_request_line(line=request_lines[0])
        headers = self.parse_header_lines(lines=request_lines[1:])
        host = headers.get('Host')

        server_name = self.socket.getsockname()

        if not host:
            raise HTTPError(400, 'Bad request', 'Host header is missing')
        if host not in (server_name[0], f'{server_name[0]}:{server_name[1]}'):
            raise HTTPError(404, 'Not found')
        return Request(method, target, version, headers)

    @staticmethod
    def parse_request_line(line: str):
        words = line.split()

        if len(words) != 3:
            raise HTTPError(400, 'Bad request', 'Malformed request line')

        method, target, ver = words

        if ver != 'HTTP/1.1':
            raise HTTPError(505, 'HTTP Version Not Supported')

        return method, target, ver

    @staticmethod
    def parse_header_lines(lines: [str]) -> [Message]:
        headers = "\n".join(lines)
        headers = HeadersParser().parsestr(headers)

        return headers

    def handle_request(self, request: Request) -> Response:
        if request.path == self.Constants.assessments_path and request.method == HTTPMethods.post:
            return self.handle_post_assessments(request.query)

        if request.path == self.Constants.assessments_path and request.method == HTTPMethods.get:
            return self.handle_get_users(request)

        raise HTTPError(404, 'Not found')

    def handle_post_assessments(self, query: Dict[str, List[Any]]) -> Response:
        assessment_title = query['title'][0]
        assessment_value = int(query['value'][0])
        self.assessments[assessment_title] = assessment_value

        return Response(204, 'Created')

    def handle_get_users(self, req):
        accept = req.headers.get('Accept')

        if 'text/html' in accept:
            contentType = 'text/html; charset=utf-8'
            body = '<html><head></head><body>'
            body += f'<div>Зачётка ({len(self.assessments)})</div>'
            body += '<ul>'

            for key, value in self.assessments.items():
                body += f'<li>#{key}, {value}</li>'

            body += '</ul>'
            body += '</body></html>'
        elif 'application/json' in accept:
            contentType = 'application/json; charset=utf-8'
            body = json.dumps(self.assessments)
        else:
            return Response(406, 'Not Acceptable')

        body = body.encode('utf-8')
        headers = [('Content-Type', contentType), ('Content-Length', len(body))]

        return Response(200, 'OK', headers, body)

    @staticmethod
    def send_response(response: Response, client_socket: socket_module.socket):
        response_file = client_socket.makefile('wb')
        status_line = f'HTTP/1.1 {response.status} {response.reason}\r\n'

        response_file.write(status_line.encode('iso-8859-1'))

        if response.headers:
            for (key, value) in response.headers:
                header_line = f'{key}: {value}\r\n'
                response_file.write(header_line.encode('iso-8859-1'))

        response_file.write(b'\r\n')

        if response.body:
            response_file.write(response.body)

        response_file.flush()
        response_file.close()

    def send_error(self, error: HTTPError, client_socket: socket_module.socket):
        try:
            status = error.status
            reason = error.reason
            body = (error.body or error.reason).encode('utf-8')
        except:
            status = 500
            reason = b'Internal Server Error'
            body = b'Internal Server Error'

        response = Response(status, reason, [('Content-Length', len(body))], body)

        self.send_response(response=response, client_socket=client_socket)


if __name__ == '__main__':
    server = HTTPServer(socket_address=Configs.server_socket_address, number_to_listening=Configs.server_listen_number)

    server.listen()
