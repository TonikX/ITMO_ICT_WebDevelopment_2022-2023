import socket
import sys
import request,response
import marks_dao
import HTTPError

class MyHTTPServer:
    def __init__(self, host, port, name, marks_dao):
        self.host = host
        self.port = port
        self.name = name
        self.marks_dao = marks_dao

    def serve_forever(self):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.bind((self.host, self.port))
        connection.listen()
        while True:
            client, addr = connection.accept()
            self.serve_client(client)

    def serve_client(self, client):
        try:
            req = self.parse_request(client)
            response = self.handle_request(req)
            self.send_response(response, client)
        except HTTPError as err:
            self.send_error(client, err)

    def parse_request(self, client):
        rfile = client.makefile("rb")
        line = rfile.readline()
        line = line.decode("utf-8")
        line = line.rsplit("\r\n")
        words = line[0].split()
        method, target, ver = words
        headers = self.parse_headers(rfile)
        if headers["Host"] not in (self.name, f'{self.host}:{self.port}'):
            raise HTTPError(404, 'not found')
        return request.request(method, target, ver, headers, rfile)

    def parse_headers(self, rfile):
        headers = dict()
        while True:
            line = rfile.readline()
            if b'\r\n'== line:
                print("found end of headers")
                break
            line = line.decode("utf-8")
            line = line.rsplit("\r\n")
            words = line[0].split(": ")
            header, value = words
            headers[header]=value
        return headers

    def handle_request(self, request):
        if  request.method == "GET" and request.path=="/marks" and request.query:
            return self.handle_get_certain_marks(request)
        elif request.method == "POST" and request.path=="/marks":
            return self.handle_post_marks(request)
        elif  request.method == "GET" and request.path=="/marks":
            return self.handle_get_marks(request)
        else: raise Exception("not found")
    
    def handle_get_certain_marks(self, request):
        path_variable = request.query
        subject = path_variable['subject'][0]
        body = self.body_builder(request, subject)
        content_type, body = body
        headers = {'Content-Type': content_type, 'Content-Length': len(body)}
        return response.response(200, "OK", headers, body)

    def handle_get_marks(self, request):
        body = self.body_builder(request)
        content_type, body = body
        headers = {'Content-Type': content_type, 'Content-Length': len(body)}
        return response.response(200, "OK", headers, body)

    def body_builder(self,request, subject=None):
        accept = request.headers['Accept']
        if 'text/html' in accept:
            content_type = "text/html; charset=utf-8"
            body = '<!DOCTYPE html>'
            body += '<html lang="en"><head><title>lol</title>'
            body+= '<link rel="icon" href="data:;base64,=">'
            body += '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">'
            body += '</head><body>'
            body += '<div>Оценки</div>'
            body +='<ul>'
            if not subject:
                marks = self.marks_dao.get_marks()
                for key in marks:
                    body+=f'<li>{key}: '
                    for mark in marks[key]:
                        body+=f'{str(mark)} '
                    body+='</li>'
            else: 
                marks = self.marks_dao.get_marks_subject(subject)
                print(marks)
                body+=f'<li>{subject}: '
                for mark in marks:
                    body+=f'{str(mark)} '
                body+='</li>'
            body+='</ul>'
            body+='</body></html>'
        return (content_type, body)

    def handle_post_marks(self, request):
        path_variables = request.query
        self.marks_dao.add(path_variables["subject"][0], path_variables["mark"][0])
        return response.response(204, "Created")

    def send_response(self, response, connection):
        wfile = connection.makefile('wb')
        status = f'HTTP/1.1 {response.status} {response.reason}\r\n'
        wfile.write(status.encode("utf-8"))
        print(status)
        if response.headers:
            for key in response.headers.keys():
                header = f'{key}: {response.headers[key]}\r\n'
                wfile.write(header.encode("utf-8"))
        print(response.headers)
        wfile.write(b'\r\n')

        if response.body:
            wfile.write(response.body.encode("utf-8"))
        print(response.body)
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
            resp = response(status, reason,
                   [('Content-Length', len(body))],
                   body)
        self.send_response(conn, resp)
        
if __name__ == '__main__':
  host = '127.0.0.1' 
  port = 14901
  name = 'example.com'
  marks_dao = marks_dao.marks_dao("marks.txt")
  serv = MyHTTPServer(host, port, name, marks_dao)
  try:
    serv.serve_forever()
  except KeyboardInterrupt:
    pass