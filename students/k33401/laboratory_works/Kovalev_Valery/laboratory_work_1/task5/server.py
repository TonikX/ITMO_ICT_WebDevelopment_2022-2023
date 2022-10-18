import socket
from Request import Request
from Response import Response
from urllib.parse import parse_qs

class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.marks = {"Web-программирование": "1",
                      "Компьютерные сети": "5",
                      "Операционные системы": "1",
                      "Иностранный язык": "1"}

    def serve_forever(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            while True:
                client, address = self.server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            self.server.close()

    def serve_client(self, client):
        try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        except Exception as e:
            print(e)
        client.close()

    def parse_request(self, data):
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    def parse_headers(self, req):
        headers = [h for h in req[1:req[1:].index("") + 1]]
        hdict = {}
        for h in headers:
            k, v = h.split(':', 1)
            hdict[k] = v
        return hdict

    def handle_request(self, req):
        try:
            if req.method == "GET" and req.path == "/":
                return self.handle_root()
            if req.method == "POST" and req.path.startswith("/api"):
                _id = int(req.query["id"][0]) - 1
                value = int(req.query["value"][0])
                if value > 5 or value < 1:
                    raise Exception("Неверное значение оценки")
                self.marks[list(self.marks.keys())[_id]] = value
                return self.handle_root()
            if req.method == "POST" and req.path.startswith("/form-request"):
                q = parse_qs(req.data[-int(req.headers["Content-Length"]):])
                _id = int(q["id"][0]) - 1
                value = int(q["value"][0])
                if value > 5 or value < 1:
                    raise Exception("Неверное значение оценки")
                self.marks[list(self.marks.keys())[_id]] = value
                return self.handle_root()
            return self.get_error(404, "Ты даже не гражданин!")
        except Exception as e:
            print(f"ERROR: {e}")
            return self.get_error(500, e)

    def send_response(self, client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    def handle_root(self):
        body = """<!DOCTYPE html><html lang="en"><head>"""
        with open("res/style.css", "r") as file:
            body += "<style>"
            body += file.read()
            body += "</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += f"<thead><tr><th>ID</tр><th>Предмет</th><th>Оценка</th></tr></thead><tbody>"
        for i, mark in enumerate(self.marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("res/form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)

    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2001, 'example.com').serve_forever()
