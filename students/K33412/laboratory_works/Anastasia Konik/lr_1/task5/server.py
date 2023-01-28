import socket

MAX_LINE = 64 * 1024


class MyHTTPServer:
    # Параметры сервера
    def __init__(self, host, port):
        self._host = host
        self._port = port

    # Запуск сервера на сокете, обработка входящих соединений
    def serve_forever(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_sock.bind((self._host, self._port))
        server_sock.listen(5)

        while True:
            client_sock, client_addr = server_sock.accept()
            try:
                self.serve_client(client_sock)
            except:
                server_sock.close()
                break

    # Обработка клиентского подключения
    def serve_client(self, client_sock):
        try:
            req_str = client_sock.recv(65536).decode("utf-8")
            method, url, params, headers, body = self.parse_request(req_str)
            resp = self.handle_request(method, url, params, headers, body)
            if resp is not None:
                self.send_response(client_sock, resp)
        except ConnectionResetError:
            client_sock = None

        if client_sock:
            client_sock.close()

    @staticmethod
    def parse_request(req_str):
        req_str.replace('\r', '')
        req_lines = req_str.split('\n')

        headers, method, url, version, body, params = dict(), "", "", "", "", ""
        body_start_idx = -1
        for i in range(0, len(req_lines)):
            line = req_lines[i]
            if i == 0:  # Если первая строка, то парсить как строку запроса
                words = line.split()  # разделяем по символам
                if len(words) != 3:  # ожидаем ровно 3 части
                    raise Exception('Malformed request line')

                method, url, version = words
                if '?' in url:
                    url, params = url.split('?')
                    params_strings = params.split("&")
                    params = dict()
                    for param_string in params_strings:
                        params[param_string.split("=")[0]] = param_string.split("=")[1]

                if version != 'HTTP/1.1':
                    raise Exception('Unexpected HTTP version')

                continue
            # Если строки заголовков или тела
            if not ":" in line:  # дальше тело
                body_start_idx = i + 1
                break

            # Еще заголовки
            headers[line.split(':')[0]] = line.split(':')[1]

        if body_start_idx != -1 and body_start_idx < len(req_lines):
            body = req_lines[body_start_idx:]

        return method, url, params, headers, body

    # Функция для обработки url в соответствии с нужным методом. В случае данной работы, нужно будет создать набор
    # условий, который обрабатывает GET или POST запрос. GET запрос должен возвращать данные. POST запрос должен
    # записывать данные на основе переданных параметров.
    @staticmethod
    def handle_request(method, url, params, headers, body):
        if not url == "/":
            return ""

        if method == "GET":
            if params == "":
                resp = "HTTP/1.1 200 OK\n\n"
                with open('index.html', 'r') as f:
                    resp += f.read()
                f.close()
                return resp

            if 'subject' in params and params['subject'] in subjects:
                subject = params['subject']
                resp = "HTTP/1.1 200 OK\n\n"
                resp += f"<html><head><title>Journal for {subject}</title></head><body>"
                resp += f"<p>{subject}: "
                for grade in subjects[subject]:
                    resp += f"{grade}, "
                resp = resp[:-2]
                resp += "</p>"
                resp += "</body></html>"
                return resp

            raise "invalid get request"

        if method == "POST":
            body_kvps = body[0].split('&')
            body_params = dict()
            for kvp in body_kvps:
                body_params[kvp.split('=')[0]] = kvp.split('=')[1]

            if 'subject' in body_params and 'grade' in body_params and len(body_params) == 2:
                subject = body_params['subject'].strip()
                grade = body_params['grade'].strip()
                if grade != '' and subject != '':
                    if subject not in subjects:
                        subjects[subject] = []

                    subjects[subject].append(grade)

            resp = "HTTP/1.1 200 OK\n\n"
            resp += "<html><head><title>Journal</title></head><body>"
            for subject in subjects:
                resp += f"<p>{subject}: "
                for grade in subjects[subject]:
                    resp += f"{grade}, "
                resp = resp[:-2]
                resp += "</p>"
            resp += "</body></html>"
            return resp

    # Функция для отправки ответа. Необходимо записать в соединение status line вида HTTP/1.1 <status_code> <reason>.
    # Затем, построчно записать заголовки и пустую строку, обозначающую конец секции заголовков.
    @staticmethod
    def send_response(client_sock, resp):
        client_sock.sendall(resp.encode("utf-8"))


if __name__ == '__main__':
    host = 'localhost'
    port = 9091
    serv = MyHTTPServer(host, port)
    subjects = dict()
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        pass
