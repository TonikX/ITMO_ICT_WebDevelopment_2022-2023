import socket
MAX_LINE = 128 * 512
MAX_HEADERS = 200
class HTTServer:
    def __init__(self, host, port, server_name):
        self._host = host
        self._port = port
        self._server_name = server_name
        # Словарь для хранения оценок по дисциплинам
        self._discipline = {}
    def serve_forever(self):
        # Создание сокета для сервера
        serv_socket = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        try:
            # Привязка соксета к хосту и порту
            serv_socket.bind((self._host, self._port))
            # Начало прослушивания порта
            serv_socket.listen()
            while True:
                # Принятие нового соединения
                conn, _ = serv_socket.accept()
                try:
                    # Обслуживание клиента
                    self.serve_client(conn)
                except Exception as e:
                    print('Ошибка обслуживания клиента:', e)
        finally:
            # Закрытие сокета сервера
            serv_socket.close()

    def serve_client(self, conn):
        # Парсинг запроса клиента
        method, url_address, parameters, ver, headers = self.parse_request(conn)
        # Обработка запроса и формирование ответа
        resp = self.handle_request(method, url_address, parameters)
        # Отправка ответа клиенту
        self.send_response(conn, resp)

    def parse_request(self, conn):
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
        headers = []
        while True:
            line = rfile.readline(MAX_LINE + 1)

            if line in (b'\r\n', b'\n', b''):
                break

            headers.append(line)

        return headers

    def handle_request(self, method, url_address, parameters):
        print('Обработка запроса')
        if url_address == '/grades' and method == 'POST':
            return self.post_grades(parameters)

        if url_address == '/grades' and method == 'GET':
            return self.get_grades(parameters)

    def post_grades(self, parameters):
        # Обработка POST-запроса для добавления оценки
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
            body += f'<li>* {u} {self._discipline[parameters["discipline"]][u]}</li>'
        body += '</ul>'
        body += '</body></html>'

        body = body.encode('utf-8')
        headers = [('Content-Type', content_type),
                   ('Content-Length', len(body))]
        return [200, 'OK', headers, body]

    def send_response(self, conn, resp):
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

# Определение хоста, порта и имени сервера
host = socket.gethostname()
port = 8080
name = 'server'
# Создание сервера и запуск его бесконечного цикла обслуживания клиентов
serv = HTTPServer(host, port, name)
try:
    serv.serve_forever()
except KeyboardInterrupt:
    pass
