import socket 
 
 
class MyHTTPServer: 
    def __init__(self, host, port): 
        self._host = host 
        self._port = port 
        self._marks = [] 
        self._subjects = [] 
 
    def serve_forever(self): 
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        try: 
            serv_sock.bind((self._host, self._port)) 
            serv_sock.listen() 
            while True: 
                cl, _ = serv_sock.accept() 
                try: 
                    self.serve_client(cl) 
                except Exception as e: 
                    print('Client serving failed', e) 
        finally: 
            serv_sock.close() 
 
    def serve_client(self, conn): 
        data = conn.recv(16384) 
        data= data.decode('utf8') 
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
                resp = "HTTP/1.1 200 OK\n\n" 
                with open('task5_index.html', 'r') as file: 
                    resp += file.read() 
                return resp 
 
            if method == 'POST': 
                resp = "HTTP/1.1 200 OK\n\n" 
                params = body.split('&') 
                for a in params: 
                    if a.split('=')[0] == 'subject': 
                        self._subjects.append(a.split('=')[1]) 
                    if a.split('=')[0] == 'grade': 
                        self._marks.append(a.split('=')[1]) 
 
                resp += "<html><head><title>Journal</title></head><body><ol>" 
                for s, m in zip(self._subjects, self._marks): 
                    resp += f"<p>Subject: {s}, Grade: {m}</p>" 
                resp += "</ol></body></html>" 
                return resp 
 
    def send_response(self, conn, resp): 
        conn.send(resp.encode('utf8')) 
 
 
if __name__ == '__main__':
    host ='localhost' 
    port = 2222 
 
    serv = MyHTTPServer(host, port) 
    try: 
        serv.serve_forever() 
    except KeyboardInterrupt: 
        pass
