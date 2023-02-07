import socket
from os import path
from pathlib import Path
import webbrowser
from urllib.parse import urlparse, parse_qs


class MyHTTPServer:
    # Параметры сервера

    def __init__(self, host='localhost', port=0, name="My HTTP Server"):
        self.host = host
        self.port = port
        self.name = name
        self.data = {}

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
        print("Incoming connection from:", client_address)

        self.handle_request(connection)

        return connection

    def parse_request(self, connection):
        # 3. функция для обработки заголовка http+запроса. Python, сокет
        # предоставляет возможность создать вокруг него некоторую обертку,
        # которая предоставляет file object интерфейс. Это дайте возможность
        # построчно обработать запрос. Заголовок всегда - первая строка.
        # Первую строку нужно разбить на 3 элемента  (метод + url + версия протокола).
        # URL необходимо разбить на адрес и параметры (isu.ifmo.ru/pls/apex/f?p=2143,
        # где isu.ifmo.ru/pls/apex/f, а p=2143 - параметр p со значением 2143)
        method, path, protocol, body = self.parse_headers(connection)
        href = path.split('?')[0]

        if method == 'GET':
            query_dict = parse_qs(urlparse(path).query)
        elif method == 'POST':
            query_dict = parse_qs(body)

        return method, href, query_dict

    def parse_headers(self, connection):
        # 4. Функция для обработки headers. Необходимо прочитать все заголовки после
        # первой строки до появления пустой строки и сохранить их в массив.
        data = connection.recv(2048)
        data = data.decode('utf-8')

        method, path, protocol = data.split('\n')[0].split(' ')
        body = data.split('\r\n\r\n')[1]

        return method, path, protocol, body

    def handle_request(self, connection):
        # 5. Функция для обработки url в соответствии с нужным методом. В случае
        # данной работы, нужно будет создать набор условий, который обрабатывает GET
        # или POST запрос. GET запрос должен возвращать данные. POST запрос должен
        # записывать данные на основе переданных параметров.
        method, href, query_dict = self.parse_request(connection)

        if (method == "GET" and href == "/"):
            pass
        elif (method == "POST" and href == "/add"):
            for key, value in query_dict.items():
                if key not in self.data:
                    self.data[key] = value
                else:
                    self.data[key].append(value[0])

        self.send_response(connection)

    def send_response(self, connection):
        # 6. Функция для отправки ответа. Необходимо записать в соединение status line
        # вида HTTP/1.1 <status_code> <reason>. Затем, построчно записать заголовки и
        # пустую строку, обозначающую конец секции заголовков.
        response_type = "HTTP/1.1 200 OK\n"
        headers = "Content-Type: text/html; charset=utf-8\n\n"

        with open(index_file, 'r', encoding="utf-8") as file:
            body = file.read()
        parsed_body = self.insert_template_vars(
            body, {"table": generate_table(self.data)})

        response = response_type + headers + parsed_body
        connection.sendall(response.encode('utf-8'))

    def insert_template_vars(self, body, variables={"table": "hello", "wtf": "1"}):
        """ Replaces `{{ variable_name }}` in the body with the provided string value from dict of variables """
        cursor = 0
        while True:
            index_start = body.find("{{", cursor)
            if (index_start != -1):
                index_end = body.find("}}", cursor)
                if (index_end == -1):
                    raise Exception(
                        f"Could not find closing brackets at {cursor}")

                var = body[index_start + 2:index_end].strip(' ')
                cursor = index_end + 2

                if var in variables:
                    body = body[:index_start] + \
                        variables[var] + body[index_end + 2:]
                    cursor = index_start + len(variables[var])

            else:
                break
        return body


def generate_table(data={}):
    table = ""
    if (data):
        table_headings = []
        table_row_cells = []
        for key, value in data.items():
            table_headings.append(f'<th>{key.title()}</th>')
            for cell in value:
                table_row_cells.append(f'<td>{cell}</td>')

        split_every = len(table_row_cells) // len(table_headings)
        rows = [table_row_cells[i::split_every] for i in range(split_every)]

        nl = '\n'
        table_rows = []
        for row in rows:
            table_row = "<tr>" + nl.join(row) + "</tr>"
            table_rows.append(table_row)

        table = f"""
            <table>
                <tr>
                    {nl.join(table_headings)}
                </tr>
                {nl.join(table_rows)}
            </table>
        """
    return table


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
