import socket
 
grades = {}
 
 
class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
 
    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
        try:
            serv_sock.bind((self.host, self.port))
            serv_sock.listen()
 
            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Fail', e)
        finally:
            serv_sock.close()
 
    def serve_client(self, client):
        try:
            req = self.parse_request(client)
            resp = self.handle_request(req)
            self.send_response(client, resp)
        except ConnectionResetError:
            client = None
 
        if client:
            client.close()
 
    def parse_request_line(self, rfile):
        line = rfile.readline()
        line = line.decode('utf-8')
        return line.split()
 
    def parse_request(self, conn):
        rfile = conn.makefile('rb')
        method, target, ver = self.parse_request_line(rfile)
 
        request = {'data': {}, 'method': method}
        if '?' in target:
            request['method'] = 'POST'
            values = target.split('?')[1].split('&')
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
        content_type = 'text/html; charset=utf-8'
        body = '<html><head><style>body {background-color:pink}</style></head><body>'
        body += '<form>Предмет<br><input name="discipline" /><br><br>Оценки<br><input name="grade"/><br><br><input type="submit"></form> <table> <tr> <th>Дисциплина</th> <th>Оценки</th> </tr> '
 
        for subject in grades:
            body += f'<tr> <th>{subject}</th> <th> {grades[subject]}</th> </tr>'
        body += '</body></html>'
        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return Response(200, 'OK', headers, body)
 
    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']
 
        if discipline not in grades:
            grades[discipline] = []
 
        grades[discipline].append(grade)
 
        return self.handle_get()
 
    def send_response(self, conn, resp):
        rfile = conn.makefile('wb')
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
    serv = MyHTTPServer('127.0.0.1', 1025)
    serv.serve_forever()