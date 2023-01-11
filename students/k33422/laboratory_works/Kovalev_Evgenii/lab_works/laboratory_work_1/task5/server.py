import socket

class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body

class MyHTTPServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.marks = {}

    def serve_forever(self):
        server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        address = (self.host, self.port)

        try:
            server.bind(address)
            server.listen()
            while True:
                client, address = server.accept()
                self.serve_client(client)
        except KeyboardInterrupt:
            server.close()

    def serve_client(self, client):
        try:
            data = client.recv(4096).decode("utf-8")
            request = self.parse_request(data)
            result = self.handle_request(request)
            self.send_response(client, result)
        except Exception as e:
            print('Client serving failed', e)
        client.close()

    def parse_request(self, data):
        request = data.rstrip('\r\n')
        text = request[:data.index("\n")].split()

        if len(text) != 3:
            raise Exception('Malformed request line')

        method, target, version = text
        if version != 'HTTP/1.1':
            raise Exception('Unexpected HTTP version')

        request = {'data': {}, 'method': method}
        if '?' in target:
            request['method'] = 'POST'
            data = target.split('?')[1].split('&')
            for value in data:
                index, info = value.split('=')
                request['data'][index] = info

        return request

    def handle_request(self, request):
        if request['method'] == 'POST':
            return self.handle_post(request)
        else:
            return self.handle_get()

    def handle_get(self):
        type = "text/html; charset=utf-8"
        first_settings = "<html><head><style></style></head><body>"
        course = "<form><label>Name of discipline: </label><input name='course' /><br><br>"
        points = "<label>Number of points: </label><input name='points' /><br><br>"
        button = "<input type='submit'></form>"
        body = first_settings + course + points + button
        for course_name in self.marks:
            body += f"<div><span>{course_name}: {self.marks[course_name]}</span></div>"
        second_settings = "</body></html>"
        body += second_settings
        body = body.encode("utf-8")
        headers = [("Content-Type", type),
                   ("Content-Length", len(body))]
        return Response(200, "OK", headers, body)

    def handle_post(self, request):
        course = request["data"]["course"]
        points = request["data"]["points"]

        if course not in self.marks:
            self.marks[course] = []

        self.marks[course].append(points)

        return self.handle_get()

    def send_response(self, connection, response):
        file = connection.makefile('wb')
        status_line = f"HTTP/1.1 {response.status} {response.reason}\r\n"
        status_line = status_line.encode("utf-8")
        file.write(status_line)

        if response.headers:
            for (key, value) in response.headers:
                header_line = f"{key}: {value}\r\n"
                file.write(header_line.encode("utf-8"))

        file.write(b"\r\n")

        if response.body:
            file.write(response.body)

        file.flush()
        file.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 1405
    server = MyHTTPServer(host, port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass