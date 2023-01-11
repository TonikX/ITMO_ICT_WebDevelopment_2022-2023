import socket


class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._marks = dict()

    def serve_forever(self):
        serv_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            proto=0)

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
        try:
            method, url, headers = self.parse_request(conn)
            resp = self.handle_request(method, url)
            self.send_response(conn, resp, headers)
        except ConnectionResetError:
            conn = None

        if conn:
            conn.close()

    def parse_request(self, conn):
        if conn:
            data = conn.recv(16384).decode(
                'utf-8').replace('\r', '').split('\n')
            method, url, _ = data[0].split()
            headers = data[1: data.index('')]
            return method, url, headers

    def get_params(self, url):
        if '?' in url:
            i = url.index('?')
            params = {param.split('=')[0]: param.split('=')[1]
                      for param in url[i+1:].split('&') if param}
            url = url[:i].split('/')[1:]
        else:
            url = url.split('/')[1:]
            params = None
        return url, params

    def handle_request(self, method, url):
        url, params = self.get_params(url)
        print('-------------------------')
        print(url, params)
        if method == 'GET':
            resp = "HTTP/1.1 200 OK\n\n"
            body = '<!DOCTYPE html><html lang="en"><head><html><head><title>Journal</title></head></html><body>'
            if url[0] == 'marks':
                if len(url) == 1:
                    for subj in self._marks:
                        body += f"<b>{subj}</b> : {self._marks[subj]}</br></body></html>"
                elif len(url) == 2:
                    if url[1] in self._marks:
                        body += f"<b>{url[1]}</b> : {self._marks[url[1]]}</body></html>"
                    else:
                        body += '<h1>404 ERROR</h1></body></html>'
            else:
                body += '<h1>Wrong address</h1></body></html>'
            return resp + body

        elif method == 'POST':
            resp = "HTTP/1.1 201 Created\n\n"
            if url[0] == 'marks' and params:
                if 'subject' in params and 'mark' in params:
                    self._marks[params['subject']] = params['mark']
            return resp

    def send_response(self, conn, resp, headers):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 9090

    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
