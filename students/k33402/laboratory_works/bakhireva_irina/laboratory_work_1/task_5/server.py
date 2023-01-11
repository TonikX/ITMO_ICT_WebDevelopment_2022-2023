import socket


class MyHTTPServer:

    # Server parameters
    def __init__(self, host, port):
        self._host = host
        self._port = port

    # Starting the server on a socket, processing incoming connections
    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        try:
            sock.bind((self._host, self._port))
            sock.listen()
            while True:
                conn, _ = sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            sock.close()

    # Processing client connection
    def serve_client(self, conn):
        data = conn.recv(18456)
        data = data.decode('utf-8')
        target, method = self.parse_request(data)
        headers, body = self.parse_headers(data)
        resp = self.handle_request(target, method, body)
        self.send_response(conn, resp)

    # Processing request
    def parse_request(self, msg):
        msg = msg.replace('\r', '')
        req_line = msg.split('\n')
        method, target, protocol = req_line[0].split()
        return target, method

    # Processing headers
    def parse_headers(self, msg):

        msg = msg.replace('\r', '')
        hd_line = msg.split('\n')
        i = hd_line.index('')
        hd = hd_line[1:i]
        body = hd_line[-1]
        return hd, body

    # A function for processing the url according to the desired method.
    # The GET request should return data. The POST request should record data based on the passed parameters.

    def handle_request(self, target, method, body):
        if target == "/":
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


            if method == "GET":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html') as f:
                    resp += f.read()
                return resp

    # Sending a response
    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    subjects = []
    marks = []

    serv = MyHTTPServer('localhost', 9091)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
