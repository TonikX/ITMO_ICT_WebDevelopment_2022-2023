import socket


class MyHTTPServer:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.grade = []


    def serve_forever(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.host, self.port))
        sock.listen()
        while True:
            client_socket, _ = sock.accept()
            self.serve_client(client_socket)


    def serve_client(self, client_socket):
        data = client_socket.recv(4096).decode('utf-8')
        request = self.parse_request(data)
        response = self.handle_request(request)
        if response:
            client_socket.send(response.encode('utf-8'))
            client_socket.close()


    def parse_request(self, data):
        data_split = data.split('\r\n')
        print(f"data split : {data_split}")
        headers = data_split[0].split()
        print(f"Headers : {headers}")
        body = data_split[-1]
        request = dict()

        if len(headers) == 3:

            request.update(
                {"method": headers[0], "url": headers[1], "version": headers[2]})

            if "&" in body:
                parametre = body.split("&")
                request.update({"parametrs": parametre})
                return request
            else:
                request.update({"parametrs": {}})
                return request
        else:
            raise Exception("Bad request line")


    def handle_request(self, request):
        print(request)
        response = f"{request['version']} 200 OK\n\n"
        if request["url"] == "/":
            if request["method"] == "POST":
                 self.grade.extend(request["parametrs"])
            if request["method"] == "GET" or "POST":
                with open('index.html') as f:
                    response += f.read()
                    return response
        if request["url"] == "/grades":
            response += "<html><head><title>Journal</title></head><body>"
            for s in self.grade:
                response += f"<p>{s} </p>"
            response += "</body></html>"
            return response


if __name__ == "__main__":
    host = 'localhost'
    port = 8001
    myserver = MyHTTPServer(host, port)
    try:
        myserver.serve_forever()
    except KeyboardInterrupt:
        pass