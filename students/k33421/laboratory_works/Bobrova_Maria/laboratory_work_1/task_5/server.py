import socket

class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body


class MyHTTPServer:
    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.points = {"Maths": ["4"]}

    def serve_forever(self):
        try:
            self.server.bind((self.host, self.port))
            self.server.listen()
            while True:
                client, address = self.server.accept()
                self.serve_client(client)
                print(f"Сервер запущен на порту > {self.host}:{self.port}")
        except KeyboardInterrupt:
            self.server.close()

    def serve_client(self, client):
        try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
            print(f'Клиент подключился')
        except Exception:
            print(f'Клиент неожиданно отключился')
        client.close()

    def parse_request(self, data):
        #из соединения необходимо прочитать строку, т.е. последовательность байт, заканчивающуюся комбинацией \r\n
        req = data.rstrip('\r\n')
        text = req[:data.index("\n")].split()
        if len(text) != 3:
            raise Exception('Malformed request line')

        method, target, version = text
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        req = {'data': {}, 'method': method}
        if '?' in target:
            req['method'] = 'POST'
            data = target.split('?')[1].split('&')
            for value in data:
                index, info = value.split('=')
                req['data'][index] = info

        return req


    def handle_request(self, req): #в этом методе начинается обработка запросов
        if req['method'] == 'POST':
            return self.handle_post(req)
        else:
            return self.handle_get()

    def handle_post(self, req):
        course = req["data"]["course"]
        points = req["data"]["points"]
        if course not in self.points:
            self.points[course] = []
        if int(points) < 1 or int(points) > 5:
            raise Exception(f"Неправильное значение оценки")
        self.points[course].append(points)
        return self.handle_get()

    def handle_get(self):
        type = "text/html; charset=utf-8"
        first_settings = "<html><head><style></style></head><body>"
        course = "<form><label>Subject: </label><input name='course' /><br><br>"
        points = "<label>Grade: </label><input name='points' /><br><br>"
        button = "<input type='submit'></form>"
        body = first_settings + course + points + button
        for course_name in self.points:
            body += f"<div><span>{course_name}: {self.points[course_name]}</span></div>"
        second_settings = "</body></html>"
        body += second_settings
        body = body.encode("utf-8")
        headers = [("Content-Type", type),
                   ("Content-Length", len(body))]
        return Response(200, "OK", headers, body)


    def send_response(self, client, res): #отправка ответа
        file = client.makefile('wb')
        status_line = f"HTTP/1.1 {res.status} {res.reason}\r\n"
        status_line = status_line.encode("utf-8")
        file.write(status_line)
        if res.headers:
            for (index, info) in res.headers:
                header_line = f"{index}: {info}\r\n"
                file.write(header_line.encode("utf-8"))
        file.write(b"\r\n")
        if res.body:
            file.write(res.body)
        file.flush()
        file.close()


    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == "__main__":
    MyHTTPServer("localhost", 9095, "example.com").serve_forever()