import socket

GRADES = {}


class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(10)
        while True:
            cliensocket, address = server.accept()
            self.serve_client(cliensocket)

    def serve_client(self, clientsocket):
        try:
            req = self.parse_request(clientsocket)
            resp = self.handle_request(req)
            self.send_response(clientsocket, resp)
        except ConnectionResetError:
            clientsocket = None
        if clientsocket:
            clientsocket.close()


    def parse_request_line(self, rfile):
        line = rfile.readline(10**4)
        line = line.decode("utf-8")
        return line.split()

    def parse_request(self, clientsocket):
        rfile = clientsocket.makefile('rb')
        method, url, ver = self.parse_request_line(rfile)
        request = {'data': {}, 'method': method}
        if '?' in url:
            request['method'] = 'POST'
            values = url.split('?')[1].split('&')
            for value in values:
                a, b = value.split('=')
                request['data'][a] = b
        return request

    
    def handle_request(self, req):
        if req['method'] == 'POST':
            return self.handle_post(req)
        else:
            return self.handle_get()

    def handle_get(self):
        contenttype = 'text/html; charset=utf-8'
        body = '<html><head><style></style></head><body>'
        body += '<form><label>Discipline </label><input name="discipline" /><br><label>Mark </label><input name="grade"/><br><input type="submit"></form>'
        for i in GRADES:
            body += f'<div><span>{i}: {GRADES[i]}</span></div>'
        body += '</div></body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', contenttype),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)

    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in GRADES:
            GRADES[discipline] = []

        GRADES[discipline].append(grade)

        return self.handle_get()

    def send_response(self, clientsocket, resp):
        rfile = clientsocket.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        rfile.write(status_line.encode('utf-8'))

        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                rfile.write(header_line.encode('utf-8'))

        rfile.write(b'\r\n')

        if resp.body:
            rfile.write(resp.body)

        rfile.flush()
        rfile.close()


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body



if __name__ == '__main__':
    serv = MyHTTPServer('127.0.0.1', 8080)
    serv.serve_forever()