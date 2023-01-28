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
