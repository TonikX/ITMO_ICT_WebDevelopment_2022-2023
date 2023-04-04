import socket
import sys
import time


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port, name):
        self._host = host
        self._port = port
        self._server_name = name

    # 1. Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        # создание сокета
        serv_sock = socket.socket(
            socket.AF_INET,  # задаем семейство протоколов 'Интернет' (INET)
            socket.SOCK_STREAM,  # задаем тип передачи данных 'потоковый' (TCP)
            proto=0)  # выбираем протокол 'по умолчанию' для TCP, т.е. IP
        try:
            serv_sock.bind((self._host, self._port)) # привязываем созданный сокет
            serv_sock.listen() # переводим сокет в состояние ожидания подключения
            # чтения и записи данных в клиентский сокет:
            while True:
                # Бесконечно обрабатываем входящие подключения
                client, addr = serv_sock.accept()
                self.serve_client(client)
        finally:
            # закрываем сокет
            serv_sock.close()

    # 2. Обработка клиентского подключения
    def serve_client(self, client):
        try:
            # парсинг заголовка
            method, url, version, parametrs, headers = self.parse_request(client)
            # получив запрос обработаем и отправим все клиенту
            self.handle_request(method, url, headers, client, parametrs)
        except ConnectionResetError:
            client = None
        if client:
            client.close()

    # 3. функция для обработки заголовка http+запроса.Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола). URL необходимо разбить на адрес и параметры
    def parse_request(self, client):
        #получим заголовки запроса
        rfile = client.makefile('rb')
        method, url, version, parametrs= None,None,None,None
        for line in rfile: #сделала способом, который понимаю
            words = line.decode('utf-8').split()
            if len(words) != 3:  # и ожидаем ровно 3 части
                raise Exception('Malformed request line')
            method, url, version = words
            # проверим, есть ли параметры
            if ("?" in url) :
                url, parametrs = url.split('?')
            break
        #теперь прочитаем остальные строки в другой функции
        headers = self.parse_headers(rfile)
        return method, url, version, parametrs, headers


    # 4. Функция для обработки headers. Необходимо прочитать все заголовки после первой строки до появления пустой строки и сохранить их в массив.
    def parse_headers(self, rfile):
        headers = []
        for line in rfile:
            if line in (b'\r\n', b'\n', b''):
                # завершаем чтение заголовков
                break
            headers.append(line)
        return headers

    # 5. Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор условий,
    # который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен записывать данные на основе переданных параметров.
    def handle_request(self, method, url, headers, client, parametrs):
        if url == "/":
            if method == "GET":
                pass
            if method == "POST" and parametrs != None:
                data = parametrs.split('&')
                Discipline.append(data[0].split('=')[1])
                Mark.append(data[1].split('=')[1])
        self.send_response(client)
        return

    # 6. Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    def send_response(self, client):
        resp = "HTTP/1.1 200 OK\n\n"
        with open('index.html', 'r') as f:
            # запишем в ответ весь респонс
            for line in f:
                if('<div id="in_serv">\n'== line):
                    # если имеется значени в массиве, выводим их
                    for i in range(len(Discipline)):
                        resp +='<p id="in_serv"> Discipline:' + Discipline[i] +', Mark: '+ Mark[i] + '</p>'
                resp += line
        client.send(resp.encode('UTF-8'))


if __name__ == '__main__':
    host = 'localhost'
    port = 9091
    name = 'example'
    serv = MyHTTPServer(host, port, name)
    Discipline = []
    Mark = []
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass