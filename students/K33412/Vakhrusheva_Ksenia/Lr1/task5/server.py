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
