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
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Создаем объект сокета
        self.points = {"Maths": ["4"]} #первый список, отображающийся на сайте

    def serve_forever(self):
        #Обработка запросов происходит синхронно,
        #т.е. возможно обслуживать не более одного клиента в один момент времени.
        try:
            self.server.bind((self.host, self.port)) # Указываем IP и порт сервера
            self.server.listen() # Максимальное количество подключений
            while True: #Сервер в бесконечном цикле осуществляет прием входящих соединений
                client, address = self.server.accept() #Создает новый объект Socket для заново созданного подключения.
                #Каждое соединение client является клиентским сокетом.
                #Прием очередного соединения инициирует обработку HTTP-запроса serve_client(client).
                self.serve_client(client)
                print(f"Сервер запущен на порту > {self.host}:{self.port}")
        except KeyboardInterrupt: #Исключение, возникающее когда пользователь нажимает определённые клавиши прерывания процесса
            self.server.close()

    def serve_client(self, client):
        try:
            data = client.recv(1024).decode() #чтение данных с определенным кол-м байт и декодирование данных
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
            print(f'Клиент подключился')
        except Exception:
            print(f'Клиент неожиданно отключился')
        client.close()

    #Чтение и разбор (синтаксический анализе) HTTP-запроса
    def parse_request(self, data):
        #прочитали строку из соединения и разбили ее по пробелу на составляющие - метод, цель и версию
        req = data.rstrip('\r\n')
        text = req[:data.index("\n")].split() #разделяем
        if len(text) != 3: #ожидаем ровно три части
            raise Exception('Malformed request line')
        #сохраняем их в некоторую структуру данных
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

        return req #сохранили их в структуре Request

    # Обработка запросов
    #Сам метод занимается скорее диспетчеризацией запросов на основе метода и цели, чем непосредственно обработкой
    def handle_request(self, req):
        if req['method'] == 'POST':
            return self.handle_post(req)
        else:
            return self.handle_get()

    #метод создания предмета и оценки
    def handle_post(self, req):
        course = req["data"]["course"]
        points = req["data"]["points"]
        if course not in self.points:
            self.points[course] = []
        if int(points) < 1 or int(points) > 5:
            raise Exception(f"Неправильное значение оценки")
        self.points[course].append(points)
        return self.handle_get()

    #возвращение списка оценок на предмет
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

    #Отправка ответа
    def send_response(self, client, res):
        file = client.makefile('wb')
        #записываем в соединение status line вида HTTP/1.1 <status_code> <reason>
        status_line = f"HTTP/1.1 {res.status} {res.reason}\r\n"
        status_line = status_line.encode("utf-8")
        file.write(status_line)
        #построчно записываем заголовки и не забываем пустую строку, обозначающую конец секции заголовков
        if res.headers:
            for (index, info) in res.headers:
                header_line = f"{index}: {info}\r\n"
                file.write(header_line.encode("utf-8"))
        file.write(b"\r\n")
        #При наличии тела ответа, ожидаем, что оно уже представлено последовательностью байт и просто отправляем его в сокет
        if res.body:
            file.write(res.body)
        file.flush()
        file.close()

    #В случае ошибки на любом из этапов, обработка заканчивается отправкой сообщения об ошибке
    def get_error(self, code, text):
        return Response(code, "OK", "Content-Type: text/html; charset=utf-8", text)


if __name__ == "__main__":
    MyHTTPServer("localhost", 9095, "example.com").serve_forever()