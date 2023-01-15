import socket
from request import Request
from response import Response
from subject import Subject


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.subjects = [Subject("Test Subject", [5, 4, 3])]

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
        return Request(
            method=method, target=target, version=ver, headers=headers, data=data
        )

    def parse_headers(self, req):
        headers = [h for h in req[1 : req[1:].index("") + 1]]
        header_dict = {}
        for header in headers:
            key, value = header.split(":", 1)
            header_dict[key] = value
        return header_dict

    def handle_request(self, req):
        try:
            if req.method == "GET" and req.path == "/":
                return self.handle_root()

            elif req.method == "POST" and req.path.startswith("/api"):
                name = str(req.query["name"][0])
                value = int(req.query["mark"][0])
                for subject in self.subjects:
                    if subject.name == name:
                        subject.add_mark(value)
                        return self.handle_root()
                self.subjects.append(Subject(name, [value]))
                return self.handle_root()

            return self.get_error(404, "Error 404: Not Found")
        except Exception as e:
            print(f"ERROR: {e}")
            return self.get_error(500, e)

    def send_response(self, client, res):
        client.sendall(
            f"HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}".encode()
        )

    def handle_root(self):
        body = """<!DOCTYPE html><html lang="en"><head>"""
        body += (
            """<meta charset="UTF-8"><title>Super Cool Page</title></head><body><table>"""
        )
        body += f"<thead><tr><th>Subject</th><th>Marks</th></tr></thead><tbody>"
        for subject in self.subjects:
            body += f"<tr><td>{subject.name}</td><td>{', '.join(str(x) for x in subject.marks)}</td></tr>"
        body += """</tbody></table>"""
        body += """</body></html>"""
        return Response(200, "OK", "Content-Type: text/html; charset=utf-8", body)

    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == "__main__":
    MyHTTPServer("localhost", 9095, "example.com").serve_forever()
