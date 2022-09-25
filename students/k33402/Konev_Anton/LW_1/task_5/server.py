import socket
import sys


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self._server_name = name

    # 1. Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        try:
            serv_sock.bind((self._host, self._port))
            serv_sock.listen()

            while True:
                client, addr = serv_sock.accept()
                self.serve_client(client)

        finally:
            serv_sock.close()

    # 2. Обработка клиентского подключения
    def serve_client(self, client):
        try:
            method, url, version, params, headers = self.parse_request(client)
            self.handle_request(method, url, headers, client, params)
        except ConnectionResetError:
            client = None
        if client:
            client.close()

    # 3. функция для обработки заголовка http+запроса.Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола). URL необходимо разбить на адрес и параметры
    def parse_request(self, client):
        rfile = client.makefile('rb')
        method, url, version, params = None, None, None, None
        for line in rfile:
            words = line.decode('utf-8', errors='ignore').split()
            if len(words) != 3:
                raise Exception('Malformed request line')
            method, url, version = words
            # проверяем, есть ли параметры
            if "?" in url:
                url, params = url.split('?')
            break
        headers = self.parse_headers(rfile)
        return method, url, version, params, headers

    # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    @staticmethod
    def parse_headers(rfile):
        headers = []
        for line in rfile:
            if line in (b'\r\n', b'\n', b''):
                break
            headers.append(line)
        return headers

    # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор условий,
    # который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
    def handle_request(self, method, url, headers, client, params):
        if url == "/":
            if method == "GET":
                pass
            if method == "POST" and params is not None:
                data = params.split('&')
                discipline.append(data[0].split('=')[1])
                mark.append(data[1].split('=')[1])
        self.send_response(client)
        return

    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    @staticmethod
    def send_response(client):
        resp = "HTTP/1.1 200 OK\n\n"
        with open('index.html', 'r') as f:
            for line in f:
                if '<div id="on__server">\n' == line:
                    for i in range(len(discipline)):
                        resp += '<p id="on__server"> Discipline: ' + discipline[i] + ', Mark: ' + mark[i] + '</p>'
                resp += line
        client.send(resp.encode('UTF-8'))


if __name__ == '__main__':
    host = 'localhost'
    port = 9095
    name = 'example'
    serv = MyHTTPServer(host, port, name)
    discipline = []
    mark = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
