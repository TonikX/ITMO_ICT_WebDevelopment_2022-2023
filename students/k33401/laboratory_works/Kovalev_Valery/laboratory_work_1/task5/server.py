import socket
import sys
from Request import Request
from Response import Response


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
        data = client.recv(1024).decode()
        req = self.parse_request(data)
        res = self.handle_request(req)
        if res:
            self.send_response(client, res)
        else:
            self.send_error(client)

    def send_error(self, client):
        client.send(b'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=utf-8\r\n\r\nSome error')

    def parse_request(self, data):
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        return Request(method, target, ver, data)

    def handle_request(self, req):
        print(req.path)
        try:
            if req.method == "GET" and req.path == "/":
                return self.handle_root()
            if req.method == "POST" and req.path.startswith("/api"):
                _id = int(req.query["id"][0]) - 1
                value = req.query["value"][0]
                self.marks[list(self.marks.keys())[_id]] = value
                return self.handle_root()
        except Exception as e:
            print(f"ERROR: {e}")
            return self.error_500(e)

    def send_response(self, client, res):
        client.send(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    def handle_root(self):
        body = """<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Start 
        page</title></head><body><table><tbody>"""
        body += f"<tr><td>ID</td><td>Предмет</td><td>Оценка</td></tr>"
        for i, mark in enumerate(self.marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table></body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)

    def error_500(self, text):
        return Response(500, "Internal Server Error", "Content-Type: text/html; charset=utf-8", text)


if __name__ == '__main__':
    MyHTTPServer('127.0.0.1', 2001, 'example.com').serve_forever()
