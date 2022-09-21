import socket
from os import path
from pathlib import Path
import webbrowser
import sys
from urllib.parse import urlparse, parse_qs


class MyHTTPServer:
    # Параметры сервера

    def __init__(self, host='localhost', port=0, name="My HTTP Server"):
        self.host = host
        self.port = port
        self.name = name

    def serve_forever(self):
        # 1. Запуск сервера на сокете, обработка входящих соединений
        # TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Ensures that port is always ready to be used again
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.host, self.port))

        # Makes keyboard interrupt possible at all times
        sock.settimeout(1.0)
        sock.listen(10)

        url = f'http://{sock.getsockname()[0]}:{sock.getsockname()[1]}'
        print(
            f"Started server at {url}")
        webbrowser.open(url)

        while True:
            try:
                connection = self.serve_client(sock)
            # Handle timeout
            except IOError:
                continue

            except KeyboardInterrupt:
                print("Stopping server...")
                if connection:
                    connection.close()
                break

        sock.close()

    def serve_client(self, sock):
        # 2. Обработка клиентского подключения
        try:
            connection, client_address = sock.accept()
        # Handle timeout
        except IOError:
            raise IOError
        self.parse_request(connection)
        print("Incoming connection from:", client_address)

        self.send_response(connection)

        return connection

    def parse_request(self, connection):
        # 3. функция для обработки заголовка http+запроса. Python, сокет
        # предоставляет возможность создать вокруг него некоторую обертку,
        # которая предоставляет file object интерфейс. Это дайте возможность
        # построчно обработать запрос. Заголовок всегда - первая строка.
        # Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола).
        # URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143,
        # где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
        method, path, protocol = self.parse_headers(connection)
        query_dict = parse_qs(urlparse(path).query)
        href = path.split('?')[0]

        self.handle_request(method, href, query_dict)

    def parse_headers(self, connection):
        # 4. Функция для обработки headers. Необходимо прочитать все заголовки после
        # первой строки до появления пустой строки и сохранить их в массив.
        data = connection.recv(2048)
        data = data.decode('utf-8')

        method, path, protocol = data.split('\n')[0].split(' ')

        return method, path, protocol

    def handle_request(self, method, href, query_dict):
        # 5. Функция для обработки url в соответствии с нужным методом. В случае
        # данной работы, нужно будет создать набор условий, который обрабатывает GET
        # или POST запрос. GET запрос должен возвращать данные. POST запрос должен
        # записывать данные на основе переданных параметров.
        if (method == "GET"):
            pass
        elif (method == "POST"):
            pass

    def send_response(self, connection):
        # 6. Функция для отправки ответа. Необходимо записать в соединение status line
        # вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и
        # пустую строку, обозначающую конец секции заголовков.

        response_type = "HTTP/1.1 200 OK\n"
        headers = "Content-Type: text/html; charset=utf-8\n\n"

        with open(index_file, 'r', encoding="utf-8") as file:
            body = file.read()

        response = response_type + headers + body
        connection.sendall(response.encode('utf-8'))


if __name__ == '__main__':
    # Makes consistent path to work directory in case of
    # 1. Running .py file directly `python server.py`
    # 2. Running .py file from another directory `python ./someComplicatedPath/server.py`
    # 3. Running cell from .ipynb notebook
    ipynb_path = "./Task 5"
    if "__file__" in globals():
        dirname = path.dirname(__file__)
    else:
        dirname = Path(path.abspath("") + ipynb_path)
    index_file = Path(dirname) / 'index.html'

    serv = MyHTTPServer()

    serv.serve_forever()
