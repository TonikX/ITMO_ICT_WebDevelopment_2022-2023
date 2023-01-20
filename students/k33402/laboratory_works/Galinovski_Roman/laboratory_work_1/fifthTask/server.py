import socket

class MyHTTPServer:

    def __init__(self, host, port, name):
        self.host = host
        self.port = port
        self.name = name
        self.marks = []

    def serveForever(self):

        serveSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serveSocket.bind((self.host, self.port))
        serveSocket.listen(10)
        print('hi')
        while True:
            clientSocket, address = serveSocket.accept()
            self.serveClient(clientSocket)

    def serveClient(self, sock):

        data = sock.recv(4096).decode("utf-8")
        request = self.parseRequest(data)
        response = self.handleRequest(request)
        sock.send(response.encode())

    def parseRequest(self, data):

        requestLine = data.split('\r\n')[0]
        words = requestLine.split()
        if len(words) == 3:
            try:
                par = data.split('\r\n')[-1]
                param = {}
                for p in par.split("&"):
                    param[p[:p.index('=')]] = p[p.index('=') + 1:]
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": param}
            except:
                req = {"method": words[0], "url": words[1], "version": words[2], "parametrs": {}}
        else:
            raise Exception('Malformed request line')
        print(req)
        return req

    def parseHeaders(self, data):
        lines = data.split('\r\n')[1:]
        headers = {}
        for line in lines:
            parts = line.split(': ')
            headers[parts[0]] = parts[1]
        return headers

    def handleRequest(self, request):
        response = f"{request['version']} 200 OK\n\n"

        if request['method'] == 'GET' and request['url'] == "/":
            with open('index.html') as page:
                response += page.read()
        elif request['method'] == 'GET' and request['url'] == "/view":
            body = '<!DOCTYPE html>' \
               '<html lang="ru">' \
               '<head>' \
               '<meta charset="UTF-8">' \
               '<title>Оценки</title>' \
               '</head>' \
               '<body>' \
               '<table align="center" width="20%" border="1">'
            for subject, mark in self.marks:
                body +=f"<tr><td>{subject}</td><td>{mark}</td></tr>"
            body += '</table></body></html>'
            response += body
        elif request['method'] == 'POST':
            self.marks.append((request['parametrs']['subject'], request['parametrs']['mark']))

        return response

if __name__ == '__main__':
    host = 'localhost'
    port = 9889
    name = 'torry-site.ru'
    serv = MyHTTPServer(host, port, name)
    try:
        serv.serveForever()
    except KeyboardInterrupt:
        pass