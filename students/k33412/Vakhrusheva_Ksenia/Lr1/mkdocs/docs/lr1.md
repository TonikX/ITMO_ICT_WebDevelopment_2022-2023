# Лабораторная работа 1
## Задача 1

* `client.py`
```python
import socket

import settings


def main():
	message = settings.client_message.encode(settings.encoding)

	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	sock.sendto(message, (settings.server_addr, settings.server_port))
	print("Client sent the message")

	data = sock.recv(settings.buffer_size)
	print(data.decode(settings.encoding))
	sock.close()


if __name__ == "__main__":
	main()

```

* `server.py`
```python
import socket

import settings


def main():
	message = settings.server_message.encode(settings.encoding)

	sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	sock.bind((settings.server_addr, settings.server_port))
	print("Server is listening")

	data, addr = sock.recvfrom(settings.buffer_size)
	print("Message from", addr)
	print(data.decode(settings.encoding))

	sock.sendto(message, addr)

	print("Server is closed")
	sock.close()


if __name__ == "__main__":
	main()

```

* `settings.py`
```python
encoding = "utf-8"
buffer_size = 1024

client_message = "Hello, server"

server_message = "Hello, client"
server_addr = "localhost"
server_port = 8080

```

## Задача 2

* `client.py`
```python
import socket

import settings


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((settings.server_addr, settings.server_port))

	while True:
		data = sock.recv(settings.buffer_size).decode(settings.encoding).strip()

		match data:
			case settings.command_input:
				number = input()
				sock.sendall(number.encode(settings.encoding))
			case settings.command_done:
				break
			case _:
				print(data)
				sock.sendall(settings.command_next.encode(settings.encoding))


if __name__ == "__main__":
	main()

```

* `server.py`
```python
import math
import socket
import typing as tp

import settings


def send_message(conn: socket, message: str, wait_for_next: bool = True):
	if not message.endswith("\n"):
		message += "\n"
	conn.sendall(message.encode(settings.encoding))

	if wait_for_next:
		data = conn.recv(settings.buffer_size)
		if not data or data.decode(settings.encoding) != settings.command_next:
			raise Exception()


def recv_digit(conn: socket, message: str, wrong_message: str) -> tp.Optional[float]:
	send_message(conn, message)

	number = None
	while number is None:
		send_message(conn, settings.command_input, wait_for_next=False)

		data = conn.recv(settings.buffer_size)
		if not data:
			return None

		try:
			t = float(data)
			if t <= 0:
				raise ValueError()
			number = t
		except ValueError:
			send_message(conn, wrong_message)
	return number


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((settings.server_addr, settings.server_port))
	sock.listen()
	print("Server is listening")

	conn, addr = sock.accept()
	print("Client", addr, "connected")
	send_message(conn, "Теорема Пифагора")

	while True:
		a = recv_digit(conn, "Длина первого катета:", "Нужно ввести положительное число")
		if a is None:
			break

		b = recv_digit(conn, "Длина второго катета:", "Нужно ввести положительное число")
		if b is None:
			break

		c = math.sqrt(a ** 2 + b ** 2)
		send_message(conn, f"Длина гипотенузы: {c}")
		send_message(conn, settings.command_done, wait_for_next=False)
		break

	print("Server is closed")
	conn.close()


if __name__ == "__main__":
	main()

```

* `settings.py`
```python
encoding = "utf-8"
buffer_size = 1024

command_input = "input"
command_done = "done"
command_next = "next"

server_addr = "localhost"
server_port = 8080

```

## Задача 3

* `server.py`
```python
import socket

import settings


class SimpleHTTPServer:
	def __init__(self, host: str, port: int):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	def serve_forever(self):
		self.sock.bind((self.host, self.port))
		self.sock.listen()
		print("Server is listening", (self.host, self.port))

		while True:
			conn, addr = self.sock.accept()
			print("Got client", addr)
			self.serve_client(conn)

	def serve_client(self, conn: socket):
		self.send_response(conn)
		conn.close()

	def send_response(self, conn: socket):
		with open("index.html", "rb") as file:
			html = file.read()

		message = f'HTTP/1.1 200 OK\r\n' \
		          f'Content-Type: text/html; charset={settings.encoding}\r\n' \
		          f'\r\n' \
		          f'{html.decode("utf-8")}'

		conn.sendall(message.encode(settings.encoding))


if __name__ == '__main__':
	SimpleHTTPServer(settings.server_addr, settings.server_port).serve_forever()

```

* `settings.py`
```python
encoding = "utf-8"
buffer_size = 1024

server_addr = "localhost"
server_port = 8080

```

## Задача 4

* `client.py`
```python
import socket
import threading

import settings


class Client:
	def __init__(self, ip, port):
		self.running = True
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, port))
		print("Connected to the server")

		self.receive_thread = threading.Thread(target=self.receive_thread_method)
		self.receive_thread.start()

		self.send_thread = threading.Thread(target=self.send_thread_method)
		self.send_thread.start()

	def disconnect(self):
		self.running = False
		self.sock.close()
		print("Disconnected from the server")

	def send_message(self, message: str):
		self.sock.sendall(message.encode(settings.encoding))

	def receive_thread_method(self):
		print("Started receiving the messages from the server")
		while self.running:
			try:
				message = self.sock.recv(settings.buffer_size).decode(settings.encoding)
				print(message)
			except:
				self.disconnect()
				break

	def send_thread_method(self):
		while self.running:
			self.send_message(input())


if __name__ == "__main__":
	Client(settings.server_addr, settings.server_port)

```

* `server.py`
```python
import socket
import threading
from dataclasses import dataclass
from enum import Enum

import settings


class UserState(Enum):
	NONE = -1
	CONNECTED = 0
	READY = 1


@dataclass
class User:
	conn: socket = None
	state: UserState = UserState.NONE
	name: str = None


class Server:
	def __init__(self, ip, port):
		self.running = True
		self.users: list[User] = []

		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.bind((ip, port))
		self.sock.listen()
		print("Server is listening")

		self.receive()

	def stop(self):
		self.running = False
		self.sock.close()
		print("Server stopped")

	def broadcast(self, label: str, message: str, except_list: list[User] = None):
		if except_list is None:
			except_list = []

		full_message = f"{label}: {message}"
		print(full_message)

		for user in self.users:
			if user.state != UserState.READY or user in except_list:
				continue
			user.conn.sendall(full_message.encode(settings.encoding))

	def send_message(self, user: User, message: str):
		user.conn.sendall(message.encode())

	def process_user(self, conn: socket):
		user = User(conn=conn, state=UserState.CONNECTED, name="")
		self.users.append(user)
		while self.running:
			try:
				match user.state:
					case UserState.NONE:
						user.state = UserState.CONNECTED
					case UserState.CONNECTED:
						self.send_message(user, "What is your name?")
						name = conn.recv(settings.buffer_size).decode(settings.encoding)
						if not name:
							raise ValueError()

						user.name = name
						user.state = UserState.READY
						self.broadcast(user.name, "connected")
					case UserState.READY:
						message = conn.recv(settings.buffer_size).decode(settings.encoding)
						self.broadcast(user.name, message, [user])
			except:
				conn.close()
				self.users.remove(user)
				self.broadcast(user.name, "disconnected")
				break

	def receive(self):
		while self.running:
			conn, addr = self.sock.accept()
			print("Incoming connection", addr)

			thread = threading.Thread(target=self.process_user, args=(conn,))
			thread.start()


if __name__ == "__main__":
	Server(settings.server_addr, settings.server_port)

```

* `settings.py`
```python
encoding = "utf-8"
buffer_size = 1024

server_addr = "localhost"
server_port = 8080

```

## Задача 5

* `Request.py`
```python
from dataclasses import dataclass
from urllib.parse import parse_qs, urlparse, ParseResult


@dataclass
class Request:
	method: str
	target: str
	version: str
	headers: dict[str, str]
	data: str
	url: ParseResult = None
	query: dict[str, list[str]] = None
	path: str = None

	def __post_init__(self):
		self.url = urlparse(self.target)
		self.query = parse_qs(self.url.query)
		self.path = self.url.path

```

* `Response.py`
```python
from dataclasses import dataclass
from http.client import responses


@dataclass
class Response:
	status: int
	headers: dict[str, str]
	body: str
	reason: str = None

	def __post_init__(self):
		self.reason = responses[self.status]

	def get_http_response(self):
		headers = "\r\n".join([f"{key}: {value}" for key, value in self.headers.items()])
		return f"HTTP/1.1 {self.status} {self.reason}\r\n{headers}\r\n\r\n{self.body}"

```

* `server.py`
```python
import os
import socket
import typing as tp
from urllib.parse import parse_qs

import settings
from Request import Request
from Response import Response


class Grades:
	def __init__(self):
		self._grades: dict[int, int] = {}

	def set_grade(self, subject_index: int, grade: int):
		print(subject_index, grade)
		if not (0 <= subject_index < len(self.available_subjects)):
			return

		if grade not in self.available_grades:
			return

		self._grades[subject_index] = grade

	@property
	def grades(self) -> dict[int, int]:
		return self._grades

	@property
	def available_subjects(self) -> list[str]:
		return ["Низкоуровневое программирование", "Web-программирование", "Python программирование"]

	@property
	def available_grades(self) -> list[int]:
		return [1, 2, 3, 4, 5]


class SimpleHTTPServer:
	def __init__(self, host: str, port: str):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.grades = Grades()

	def serve_forever(self):
		self.sock.bind((self.host, self.port))
		self.sock.listen()
		print("Server is listening", (self.host, self.port))

		while True:
			conn, addr = self.sock.accept()
			print("Got client", addr)
			self.serve_client(conn)

	def serve_client(self, conn: socket):
		http_request = conn.recv(settings.buffer_size).decode(settings.encoding)
		request = self.parse_request(http_request)
		if request is not None:
			response = self.handle_request(request)
			self.send_response(conn, response)
		conn.close()

	def parse_request(self, http_request: str) -> tp.Optional[Request]:
		raw_request = http_request.split("\r\n")
		raw_header = raw_request[0].split(" ")
		if len(raw_header) != 3:
			return None

		method, target, version = raw_request[0].split(" ")
		headers = {
			t[0][:t[1]].strip(): t[0][t[1] + 1:].strip()
			for t in [
				(raw_header, raw_header.find(":"))
				for raw_header in raw_request[1:-1]
			]
		}
		return Request(method=method, target=target, version=version, headers=headers, data=raw_request[-1])

	def handle_request(self, request: Request):
		print("Request", request.method, request.target)
		match request:
			case Request("GET", target, version, headers, data, url, query, "/" as path):
				return self.handle_root()
			case Request("POST", target, version, headers, data, url, query, "/post" as path):
				return self.handle_post(parse_qs(data))
			case Request("GET", target, version, headers, data, url, query, path):
				if path.startswith("/assets/"):
					return self.handle_static_files(path.replace("/assets/", ""))
		return Response(404, {"Content-Type": "text/html; charset=utf-8",
		                      "Content-Length": str(len("Not found".encode(settings.encoding)))}, "Not found")

	def send_response(self, conn: socket, response: Response):
		print("Response", response.status, response.reason)
		conn.sendall(response.get_http_response().encode(settings.encoding))

	def handle_post(self, query: dict[str, list[str]]) -> Response:
		try:
			subject_index = query["subject"][0] if "subject" in query else None
			grade = query["grade"][0] if "grade" in query else None
			if subject_index and grade:
				self.grades.set_grade(int(subject_index), int(grade))
		except Exception as e:
			print(e)

		with open("templates/post.html", "rb") as file:
			html = file.read()

		return Response(
			200, {"Content-Type": "text/html; charset=utf-8"},
			html.decode("utf-8")
		)

	def handle_static_files(self, filename: str) -> Response:
		with open(os.path.join("assets", filename), "rb") as file:
			content = file.read()

		if filename.find(".") != -1:
			extension = filename.split(".")[-1]
		else:
			extension = "plain"

		return Response(
			200, {"Content-Type": f"text/{extension} charset=utf-8"},
			content.decode("utf-8")
		)

	def handle_root(self) -> Response:
		with open("templates/index.html", "rb") as file:
			html = file.read()

		subject_options = [
			f"<option value={i}>{subject}</option>"
			for i, subject in enumerate(self.grades.available_subjects)
		]
		subject_grades = "".join([
			f"<option value={grade}>{grade}</option>"
			for grade in self.grades.available_grades
		])
		grades_table = "".join(["<tr><th>Предмет</th><th>Оценка</th></tr>"] + list([
			f"<tr><td>{self.grades.available_subjects[subject_index]}</td><td>{grade}</td></tr>"
			for subject_index, grade in self.grades.grades.items()
		]))

		return Response(
			200, {"Content-Type": "text/html; charset=utf-8"},
			html.decode("utf-8").format(
				subject_options=subject_options,
				subject_grades=subject_grades,
				grades_table=grades_table
			)
		)


if __name__ == '__main__':
	SimpleHTTPServer(settings.server_addr, settings.server_port).serve_forever()

```

* `settings.py`
```python
encoding = "utf-8"
buffer_size = 1024

server_addr = "localhost"
server_port = 8080

```

