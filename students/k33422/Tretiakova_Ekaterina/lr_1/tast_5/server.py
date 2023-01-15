import socket
import sys


class MyHTTPServer:

        def __init__(self, host, port):
                self.host = host
                self.port = port

        def serve_forever(self):
                conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                conn.bind((self.host, self.port))
                conn.listen(10)
                while True:
                        client, address = conn.accept()
                        self.serve_client(client)

        def serve_client(self, client):
                text = client.recv(16384)
                text = text.decode('utf-8') # change
                url, method, headers, body = self.parse_request(text)
                resp = self.handle_request(url, method, body)
                if resp:
                        self.send_response(client, resp)

        def parse_request(self, text):
                text = text.replace('\r', '')
                lines = text.split('\n')
                method, url, protocol = lines[0].split()
                i = lines.index('')
                headers = lines[1:i]
                body = lines[-1]
                # exception
                return url, method, headers, body

        def handle_request(self, url, method, body):
                        resp = "HTTP/1.1 200 OK\n\n"
                        error = f" 400\n\nErorr"
                        if method == 'GET' and url == '/':
                                with open('index.html', 'r') as f: #change
                                        resp += f.read()
                                return resp
                        elif Exception:
                            return error
                        if method == "POST" and url == '/':
                                newbody = body.split('&')
                                for i in newbody:
                                        if i.split('=')[0] == 'subject':
                                                subjects.append(i.split('=')[1])
                                        if i.split('=')[0] == 'mark':
                                                marks.append(i.split('=')[1])
                                resp += "<html><head><title>Journal</title></head><body><table border=1>"
                                for s, m in zip(subjects, marks):
                                        resp += f"<tr><td>{s}</td><td>{m}</td></tr>"
                                resp += "</table></body></html>"
                                return resp
                        elif Exception:
                            return error


        def send_response(self, clientsocket, resp):
                clientsocket.send(resp.encode('utf-8'))


if __name__ == '__main__':
        host = '127.0.0.1'
        port = 3000
        serv = MyHTTPServer(host, port)
        subjects = []
        marks = []
        try:
                serv.serve_forever()
        except KeyboardInterrupt:
                pass