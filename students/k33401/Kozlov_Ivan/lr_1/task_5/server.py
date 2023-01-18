import socket

class MyHTTPServer:
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._database = []

    def serve_forever(self):
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self._conn.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self._conn.bind((self._host, self._port))
        self._conn.listen(10)
        while True:
            client, _ = self._conn.accept()
            self.serve_client(client)

    def serve_client(self, client):
        data = client.recv(4096).decode()
        if not data:
            return
        response = self.handle_request(data)
        client.send(response.encode())


    def parse_request(self, data):
        data = data.replace("\r", "")
        try:
            req = data[:data.index("\n")]
        except ValueError:
            req = data
            return req, "", ""
        if "\n\n" in data:
            headers, body = data[data.index("\n") + 1:].split("\n\n")
        else:
            headers, body = data[data.index("\n") + 1:], ""
        return req, headers, body


    def parse_headers(self, headers):
        headers_dict = {}
        for header in headers.split('\n'):
            if header:
                name = header[:header.index(': ')]
                value = header[header.index(': ') + 1:]
                headers_dict[name] = value
        return headers_dict


    def parse_body(self, body):
        body_dict = {}
        for elem in body.split('&'):
            name = elem[:elem.index('=')]
            value = elem[elem.index('=') + 1:].replace('+', ' ')
            body_dict[name] = value
        return body_dict

    def handle_request(self, data):
        req, headers, body = self.parse_request(data)
        method, url, ver = req.split()
        headers = self.parse_headers(headers)
        response = f"{ver} 200 OK\n\n"
        error_response = f"{ver} 400\n\nBad request"
        if method == 'GET' and url == '/index':
            with open('index.html') as f:
                response += f.read()  
        elif method == 'GET' and url == '/view':
            with open('view.html') as f:
                lines = f.readlines()
            table = [f"<tr><td>{s}</td><td>{g}</td></tr>" for s, g in self._database]
            response += '\n'.join(lines[:8]) + '\n'.join(table) + '\n'.join(lines[8:])
        elif method == 'POST' and url == '/send':
            parsed_body = self.parse_body(body)
            self._database.append((parsed_body['subject'], parsed_body['grade']))
            return response
        else:
            return error_response
        return response

    def kill(self):
        self._conn.close()


if __name__ == '__main__':
    host = "127.0.0.1"
    port = 8000
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        serv.kill() 
        raise KeyboardInterrupt

