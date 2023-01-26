import socket

GRADES = {} 


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port):
        self.host = host
        self.port = port

    # Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port)) # открытие сокета
        server.listen(10) # открытие очереди на соединение
        while True:
            cliensocket, address = server.accept() # прем соединения
            self.serve_client(cliensocket)

    # Инициирует обработку HTTP-запроса/клиенского подключения
    def serve_client(self, clientsocket):
        try:
            req = self.parse_request(clientsocket) #чтение и разбор/синтаксический анализ HTTP-запроса
            resp = self.handle_request(req) # обработка
            self.send_response(clientsocket, resp) # отправка ответа
        # В случае ошибки на любом из этапов, обработка заканчивается
        except ConnectionResetError:
            clientsocket = None
        if clientsocket:
            clientsocket.close()

    # Разбор request line 
    def parse_request_line(self, rfile):
        line = rfile.readline(10**4)
        line = line.decode("utf-8")
        return line.split() # возвращает декодированную строку разделенную на пробелы

    # Чтение и разбор/синтаксический анализ HTTP-запроса
    def parse_request(self, clientsocket):
        rfile = clientsocket.makefile('rb') # открываем файл для чтения
        method, url, ver = self.parse_request_line(rfile) # разбираем request line на метод, url и версию протокола
        request = {'data': {}, 'method': method}  
        # url необходимо разбить на адрес и параметр
        if '?' in url: 
            request['method'] = 'POST'
            values = url.split('?')[1].split('&') # разделяем для извлечения параметров
            for value in values:
                a, b = value.split('=')
                request['data'][a] = b
        return request

    # Функция для обработки запросов
    def handle_request(self, req):
        if req['method'] == 'POST': 
            return self.handle_post(req)
        else:
            return self.handle_get()

    # Возвращает список оценок, ф-я поодерживающая формат text/html
    def handle_get(self):
        contenttype = 'text/html; charset=utf-8'
        body = '<html><head><style></style></head><body>'
        body += '<form><label>Discipline </label><input name="discipline" /><br><label>Mark </label><input name="grade"/><br><input type="submit"></form>'
        for i in GRADES:
            body += f'<div><span>{i}: {GRADES[i]}</span></div>'
        body += '</div></body></html>'
        # кодируем строку в последовательность байт
        body = body.encode('utf-8')
        headers = [('Content-Type', contenttype), # Content-Type содержит секцию charset=utf-8, по которой клиенты сервера могут определить кодировку тела ответа
                   ('Content-Length', len(body))] # Content-Length, представляющий собой размер ответа, принимает значение длины уже в байтах
        return Response(200, 'OK', headers, body)

    # Записывает данные 
    def handle_post(self, request):
        discipline = request['data']['discipline']
        grade = request['data']['grade']

        if discipline not in GRADES:
            GRADES[discipline] = []

        GRADES[discipline].append(grade)

        return self.handle_get()

    # Функция для отправки ответа
    def send_response(self, clientsocket, resp):
        rfile = clientsocket.makefile('wb')
        status_line = f'HTTP/1.1 {resp.status} {resp.reason}\r\n'
        rfile.write(status_line.encode('utf-8'))

        # построчно записываем заголовок, разбитый на ключ и значение 
        if resp.headers:
            for (key, value) in resp.headers:
                header_line = f'{key}: {value}\r\n'
                rfile.write(header_line.encode('utf-8'))
        
        # записываем пустую  строку, обозначающую конец секции заголовков
        rfile.write(b'\r\n')
        
        # если есть тело ответа, ожидаем, что оно уже представлено последовательностью байт
        # и отправляем его в сокет
        if resp.body:
            rfile.write(resp.body)

        rfile.flush()
        rfile.close()


class Response:
    def __init__(self, status, reason, headers=None, body=None):
        self.status = status
        self.reason = reason
        self.headers = headers
        self.body = body



if __name__ == '__main__':
    serv = MyHTTPServer('127.0.0.1', 8080)
    serv.serve_forever()