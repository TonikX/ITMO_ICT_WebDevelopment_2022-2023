import socket

class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen(2)
        while True:
            clientsocket, _ = sock.accept()
            self.serve_client(clientsocket)

    def serve_client(self, clientsocket):
        data = clientsocket.recv(18456)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        if resp:
            self.send_response(clientsocket, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, target, protocol = lines[0].split()
        return target, method

    def parse_headers(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        i = lines.index('')
        headers = lines[1:i]
        body = lines[-1]
        return headers, body

    def handle_request(self, target, method, body):
        if target == "/":
            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

            if method == "POST":
                newbody = body.split('&')
                for a in newbody:
                    if a.split('=')[0] == 'subject':
                        subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        marks.append(a.split('=')[1])

                resp = "HTTP/1.1 200 OK\n\n"
                resp += "<html><head><title>Journal</title></head><body>"
                for s, m in zip(subjects, marks):
                    resp += f"<p>{s}: {m}</p>"
                resp += "</body></html>"
                return resp

    def send_response(self, clientsocket, resp):
        clientsocket.send(resp.encode('utf-8'))

if __name__ == '__main__':
    host = 'localhost'
    port = 8081
    serv = MyHTTPServer(host, port)
    subjects = []
    marks = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
