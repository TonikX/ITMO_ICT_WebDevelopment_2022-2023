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
