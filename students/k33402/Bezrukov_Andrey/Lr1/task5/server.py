import socket
import sys

MAX_LINE = 64 * 1024


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._subjects = []
        self._marks = []

    def serve_forever(self):
        conn = socket.socket()

        try:
            conn.bind((self._host, self._port))
            conn.listen()

            while True:
                conn, _ = conn.accept()
                try:
                    self.serve_client(conn)
                except Exception:
                    print('Client serving failed', Exception)
        finally:
            conn.close()

    def serve_client(self, conn):
        data = conn.recv(16384).decode('utf8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp is not None:
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
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as f:
                    resp += f.read()
                return resp

            if method == 'POST':
                resp = "HTTP/1.1 204 OK\n\n"

                params = body.split('&')
                for a in params:
                    if a.split('=')[0] == 'subj':
                        self._subjects.append(a.split('=')[1])
                    if a.split('=')[0] == 'mark':
                        self._marks.append(a.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, m in zip(self._subjects, self._marks):
                    resp += f"<li>Subject: {s}, Grade: {m}</li>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf8'))


if __name__ == '__main__':
    host ='localhost'
    port = 8765

    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass