import socket
from utils import Request, Response
from urllib.parse import parse_qs


class Server:
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._marks: dict[str, str] = {
            "Math": "2",
            "Linux": "3",
            "OOP": "2",
            "SQL": "2",
            "Physics": "5",
            "Web-Programming": "4"
        }

    def serve_client(self, client) -> None:
        # try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        # except Exception as e:
        #     print(e)
            client.close()

    def serve_forever(self) -> None:
        # try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, _ = self._server.accept()
                self.serve_client(client)
        # except KeyboardInterrupt:
        #     self._server.close()

    def parse_request(self, data) -> Request:
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    @staticmethod
    def parse_headers(req) -> dict[str, str]:
        headers = list(req[1:req[1:].index("") + 1])
        headers_dict = {}
        for h in headers:
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    @staticmethod
    def send_response(client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    @staticmethod
    def _generate_error(code: int, text: str) -> Response:
        return Response(code, "OK", text)

    def handle_root(self):
        body = """<!DOCTYPE html><html><head>"""
        with open("style.css", "r") as file:
            body += f"<style>{file.read()}</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += "<thead><tr><th>ID</tр><th>Subject</th><th>Score</th></tr></thead><tbody>"
        for i, mark in enumerate(self._marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", body)

    def handle_request(self, req):
        # try:
            if req.method == 'GET':
                if req.path == "/":
                    return self.handle_root()
                return self._generate_error(404, 'page not found')
            elif req.method == 'POST':
                if req.path.startswith("/form-request"):
                    query = parse_qs(req.data)
                    print(query)
                    # _id = int(query["id"][0]) - 1
                    _id = 4 - 1
                    value = int(query["value"][0])
                    if value not in range(1, 6):
                        raise ValueError("Score must be between 1, 2, 3, 4 or 5")
                    self._marks[list(self._marks.keys())[_id]] = str(value)
                    return self.handle_root()
            else:
                return self._generate_error(405, "Method not allowed")
        # except Exception as e:
        #     print(f"Exception: {e}")
        #     return self._generate_error(500, str(e))


if __name__ == '__main__':
    Server('127.0.0.1', 8091).serve_forever()
