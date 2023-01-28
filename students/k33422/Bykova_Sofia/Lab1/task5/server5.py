import socket


class MyHTTPServer:
    #параметры сервера
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self.grades = []
        self.subjects = []

    def serve_forever(self):#соед с клиентом
        TCPServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            TCPServerSocket.bind((self._host, self._port))
            TCPServerSocket.listen()
            while True:
                client, _ = TCPServerSocket.accept()
                try:
                    self.serve_client(client)
                except Exception as e:
                    print('Client serving failed', e)
        finally:
            TCPServerSocket.close()

    def serve_client(self, conn):
        data = conn.recv(16384)
        data = data.decode('utf-8')
        url, method, headers, body = self.parse_request(data)
        resp = self.handle_request(url, method, body)
        if resp:
            self.send_response(conn, resp)

    def parse_request(self, data):
        data = data.replace('\r', '')
        lines = data.split('\n')
        method, url, protocol = lines[0].split()
        end_headers = lines.index('')
        headers = lines[1:end_headers]
        body = lines[-1]
        return url, method, headers, body

    def handle_request(self, url, method, body):
        # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор условий, который обрабатывает GET или POST запрос.
        # GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
        if url == '/':
            if method == 'GET':
                resp = "HTTP/1.1 200 OK \n\n"
                with open('grades.html', 'r') as file:
                    resp += file.read()
                return resp
            if method == 'POST':
                resp = "HTTP/1.1 200 OK \n\n"
                parameter = body.split('&')
                for par in parameter:
                    if par.split('=')[0] == 'subject':
                        self.subjects.append(par.split('=')[1])
                    if par.split('=')[0] == 'grade':
                        self.grades.append(par.split('=')[1])

                resp += "<html><head><title>Journal</title></head><body><ol>"
                for s, g in zip(self.subjects, self.grades):
                    resp += f"<p>Subject: {s}, Grade: {g}</p>"
                resp += "</ol></body></html>"
                return resp

    def send_response(self, conn, resp):
        conn.send(resp.encode('utf-8'))


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 10003
    serv = MyHTTPServer(host, port)
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass