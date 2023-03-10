# Лабораторная работа №1 Мамедов Тогрул К33402

# client_1

import socket

sock = socket.socket()
sock.connect(('127.0.0.1', 9090))
sock.send('Hello, server'.encode('utf-8'))

data = sock.recv(1024)
print(data.decode('utf-8'))
sock.close()

# main

import socket
from utils import Request, Response
from urllib.parse import parse_qs


class Server:
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._marks: dict[str, str] = {
            "Math": "2",
            "Linux": "3",
            "OOP": "2",
            "SQL": "2",
            "Physics": "5",
            "Web-Programming": "4"
        }

    def serve_client(self, client) -> None:
        # try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        # except Exception as e:
        #     print(e)
            client.close()

    def serve_forever(self) -> None:
        # try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, _ = self._server.accept()
                self.serve_client(client)
        # except KeyboardInterrupt:
        #     self._server.close()

    def parse_request(self, data) -> Request:
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    @staticmethod
    def parse_headers(req) -> dict[str, str]:
        headers = list(req[1:req[1:].index("") + 1])
        headers_dict = {}
        for h in headers:
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    @staticmethod
    def send_response(client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    @staticmethod
    def _generate_error(code: int, text: str) -> Response:
        return Response(code, "OK", text)

    def handle_root(self):
        body = """<!DOCTYPE html><html><head>"""
        with open("style.css", "r") as file:
            body += f"<style>{file.read()}</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += "<thead><tr><th>ID</tр><th>Subject</th><th>Score</th></tr></thead><tbody>"
        for i, mark in enumerate(self._marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", body)

    def handle_request(self, req):
        # try:
            if req.method == 'GET':
                if req.path == "/":
                    return self.handle_root()
                return self._generate_error(404, 'page not found')
            elif req.method == 'POST':
                if req.path.startswith("/form-request"):
                    query = parse_qs(req.data)
                    print(query)
                    # _id = int(query["id"][0]) - 1
                    _id = 4 - 1
                    value = int(query["value"][0])
                    if value not in range(1, 6):
                        raise ValueError("Score must be between 1, 2, 3, 4 or 5")
                    self._marks[list(self._marks.keys())[_id]] = str(value)
                    return self.handle_root()
            else:
                return self._generate_error(405, "Method not allowed")
        # except Exception as e:
        #     print(f"Exception: {e}")
        #     return self._generate_error(500, str(e))


if __name__ == '__main__':
    Server('127.0.0.1', 8091).serve_forever()


# client_2

import socket

s = socket.socket()
s.connect(('localhost', 9090))

a, b, c = map(float, input('Введите коэффициенты квадратного уравнения').split())
s.send(','.join([str(a), str(b), str(c)]).encode('utf-8'))

answer = s.recv(1024)
print(answer.decode('utf-8'))

s.close()


# server_2

import socket
from math import sqrt

s = socket.socket()

s.bind(('127.0.0.1', 9090))
s.listen(1)
conn, addr = s.accept()

while True:
    data = conn.recv(1024)
    if not data:
        print('Got empty data')
        break

    list_of_nums = data.decode('utf-8').split(',')

    d = float(list_of_nums[1]) ** 2 - 4 * float(list_of_nums[0]) * float(list_of_nums[2])

    if d > 0:
        result = f'Корни квадратного уравнения: {round((-float(list_of_nums[1]) + sqrt(d)) / (2 * float(list_of_nums[0])), 2)} {round((-float(list_of_nums[1]) + sqrt(d)) / (2 * float(list_of_nums[0])), 2)}'
        conn.send(result.encode('utf-8'))
    elif d == 0:
        result = f'Корень квадратного уравнения: {round(-float(list_of_nums[1]) / (2 * float(list_of_nums[0])), 2)}'
        conn.send(result.encode('utf-8'))
    else:
        conn.send('Дискриминант меньше 0. Решений нет'.encode('utf-8'))
conn.close()

# client_3

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2468))
data = client.recv(20480)
print(data.decode("utf-8"))
client.close()


# server_3

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 2468))
server.listen()

while True:
    connection, address = server.accept()
    with open("index.html", 'r') as f:
        info = f.read()
    connection.sendto(f"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n{info}".encode("utf-8"), address)
    break

connection.close()

# client_4

import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2465))
user = input("Enter your nickname: ")


def receiving_message():
    while True:
        message = client.recv(8192)
        message = message.decode("utf-8")
        if message == "Whats your name?":
            client.sendto(user.encode("utf-8"), ("127.0.0.1", 2467))
        else:
            print(message)


def sending_message():
    while True:
        text = input("")
        message = f"{user}: {text}"
        client.sendto(message.encode("utf-8"), ("127.0.0.1", 2467))


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()



# server_4


import socket
import threading

host, port = "127.0.0.1", 2465
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"The chat at {host}:{port} was created")

clients = []


def send_to_everyone(message):
    for conn, name in clients:
        conn.send(f"{conn}: {message}")


def handle_message(client):
    while True:
        message = client.recv(8192)
        send_to_everyone(message)


def read_messages():
    message = "Whats your name?"
    while True:
        connection, address = server.accept()
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192).decode("utf-8")
        clients.append((connection, user))
        thread = threading.Thread(target=handle_message, args=(connection,))
        thread.start()


if __name__ == '__main__':
    read_messages()


# server

import socket
from utils import Request, Response
from urllib.parse import parse_qs


class Server:
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._server: socket.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self._marks: dict[str, str] = {
            "Math": "2",
            "Linux": "3",
            "OOP": "2",
            "SQL": "2",
            "Physics": "5",
            "Web-Programming": "4"
        }

    def serve_client(self, client) -> None:
        # try:
            data = client.recv(1024).decode()
            req = self.parse_request(data)
            res = self.handle_request(req)
            self.send_response(client, res)
        # except Exception as e:
        #     print(e)
            client.close()

    def serve_forever(self) -> None:
        # try:
            self._server.bind((self._host, self._port))
            self._server.listen()
            while True:
                client, _ = self._server.accept()
                self.serve_client(client)
        # except KeyboardInterrupt:
        #     self._server.close()

    def parse_request(self, data) -> Request:
        req = data.split("\r\n")
        method, target, ver = req[0].split(" ")
        headers = self.parse_headers(req)
        return Request(method=method, target=target, version=ver, headers=headers, data=data)

    @staticmethod
    def parse_headers(req) -> dict[str, str]:
        headers = list(req[1:req[1:].index("") + 1])
        headers_dict = {}
        for h in headers:
            k, v = h.split(':', 1)
            headers_dict[k] = v
        return headers_dict

    @staticmethod
    def send_response(client, res):
        client.sendall(f'HTTP/1.1 {res.status} OK\r\n{res.headers}\r\n\r\n{res.body}'.encode())

    @staticmethod
    def _generate_error(code: int, text: str) -> Response:
        return Response(code, "OK", text)

    def handle_root(self):
        body = """<!DOCTYPE html><html><head>"""
        with open("style.css", "r") as file:
            body += f"<style>{file.read()}</style>"
        body += """<meta charset="UTF-8"><title>Start page</title></head><body><table>"""
        body += "<thead><tr><th>ID</tр><th>Subject</th><th>Score</th></tr></thead><tbody>"
        for i, mark in enumerate(self._marks.items()):
            body += f"<tr><td>{i + 1}</td><td>{mark[0]}</td><td>{mark[1]}</td></tr>"
        body += """</tbody></table>"""
        with open("form.html", "r") as file:
            body += file.read()
        body += """</body></html>"""
        return Response(200, "OK", body)

    def handle_request(self, req):
        # try:
            if req.method == 'GET':
                if req.path == "/":
                    return self.handle_root()
                return self._generate_error(404, 'page not found')
            elif req.method == 'POST':
                if req.path.startswith("/form-request"):
                    query = parse_qs(req.data)
                    print(query)
                    _id = int(query["id"][0]) - 1
                    value = int(query["value"][0])
                    if value not in range(1, 6):
                        raise ValueError("Score must be between 1, 2, 3, 4 or 5")
                    self._marks[list(self._marks.keys())[_id]] = str(value)
                    return self.handle_root()
            else:
                return self._generate_error(405, "Method not allowed")
        # except Exception as e:
        #     print(f"Exception: {e}")
        #     return self._generate_error(500, str(e))


if __name__ == '__main__':
    Server('127.0.0.1', 8091).serve_forever()






