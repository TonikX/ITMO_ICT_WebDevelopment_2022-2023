import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.surnames = []
        self.grades = []
        self.subjects = []

    def serve_forever(self):

        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)

        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                conn, _ = serv_sock.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            serv_sock.close()

    def serve_client(self, conn):
        data = conn.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(conn, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        if url == '/':
            if method == 'GET':
                resp = "HTTP/1.1 200 OK \n\n"
                with open('grades.html', 'r') as file:
                    resp += file.read()
                return resp

            if method == 'POST':
                resp = "HTTP/1.1 204 OK \n\n"

                parameter = body.split('&')
                for par in parameter:
                    if par.split('=')[0] == 'surname':
                        self.surnames.append(par.split('=')[1])
                    if par.split('=')[0] == 'subject':
                        self.subjects.append(par.split('=')[1])
                    if par.split('=')[0] == 'grade':
                        self.grades.append(par.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, g in zip(self.surnames, self.subjects, self.grades):
                    resp += f"<li>Surname: {s}, Subject: {s}, Grade: {g}</li>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8888
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass