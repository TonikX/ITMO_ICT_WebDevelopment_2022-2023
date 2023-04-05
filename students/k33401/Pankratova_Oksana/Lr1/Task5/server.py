import socket
import sys

MAX_LINE = 64 * 1024
MAX_HEADERS = 100


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name

        self._discipline = {}

    def serve_forever(self):
        # 1. Запуск сервера на сокете, обработка входящих соединений
        serv_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        try:
            serv_socket.bind((self._host, self._port))
            serv_socket.listen()

            while True:
                conn, _ = serv_socket.accept()
                try:
                    self.serve_client(conn)
                except Exception as e:
                    print('Client serving faild', e)
        finally:
            serv_socket.close()

    def serve_client(self, conn):
        # 2. Обработка клиентского подключения

        method, url_address, parameters, ver, headers = self.parse_request(conn)
        resp = self.handle_request(method, url_address, parameters)
        self.send_response(conn, resp)

    def parse_request(self, conn):
        # 3. функция для обработки заголовка http+запроса. Python, сокет предоставляет возможность создать вокруг
        # него некоторую обертку, которая предоставляет file object интерфейс. Это дайте возможность построчно
        # обработать запрос. Заголовок всегда - первая строка. Первую строку нужно разбить на 3 элемента  (метод +
        # url + версия протокола). URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143 ,
        # где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)

        rfile = conn.makefile('rb')
        raw = rfile.readline(MAX_LINE + 1)

        req_line = str(raw, 'iso-8859-1')
        req_line = req_line.rstrip('\r\n')
        words = req_line.split()
        method, url, ver = words

        url_address, parameters = url.split("?")

        pairs = parameters.split('&')

        parameters = {}
        for pair in pairs:
            key, value = pair.split('=')
            parameters[key] = value

        headers = self.parse_headers(rfile)

        return method, url_address, parameters, ver, headers

    def parse_headers(self, rfile):
        # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления
        # пустой строки и сохранить их в массив.

        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)

        return headers

    def handle_request(self, method, url_address, parameters):
        # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать
        # набор условий, который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос
        # должен записывать данные на основе переданных параметров.

        print('handle')
        if url_address == '/grades' and method == 'POST':
            return self.post_grades(parameters)

        if url_address == '/grades' and method == 'GET':
            return self.get_grades(parameters)

    def post_grades(self, parameters):

        if parameters['discipline'] not in self._discipline.keys():
            self._discipline[parameters['discipline']] = {}

        self._discipline[parameters['discipline']][parameters['name']] = parameters['grade']

        print(self._discipline)

        return [204, 'Created']

    def get_grades(self, parameters):
        content_type = 'text/html; charset=utf-8'

        body = '<html><head></head><body>'
        body += f'<div>Дисциплинa ({parameters["discipline"]})</div>'
        body += '<ul>'
        for u in self._discipline[parameters["discipline"]].keys():
            body += f'<li>#{u} {self._discipline[parameters["discipline"]][u]}</li>'
        body += '</ul>'
        body += '</body></html>'

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return [200, 'OK', headers, body]

    def send_response(self, conn, resp):
        # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code>
        # <reason>. Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.

        wfile = conn.makefile('wb')
        status_line = f'HTTP/1.1 {resp[0]} {resp[1]}\r\n'
        wfile.write(status_line.encode('iso-8859-1'))

        if len(resp) > 2:
            for (key, value) in resp[2]:
                header_line = f'{key}: {value}\r\n'
                wfile.write(header_line.encode('iso-8859-1'))

        wfile.write(b'\r\n')

        if len(resp) > 3:
            wfile.write(resp[3])

        wfile.flush()
        wfile.close()


host = socket.gethostname()
port = 3030
name = 'myserver'
serv = MyHTTPServer(host, port, name)
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass
