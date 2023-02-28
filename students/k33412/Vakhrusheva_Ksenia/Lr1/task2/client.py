import socket

import settings


def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((settings.server_addr, settings.server_port))

	while True:
		data = sock.recv(settings.buffer_size).decode(settings.encoding).strip()

		if data == settings.command_input:
			number = input()
			sock.sendall(number.encode(settings.encoding))
		elif data == settings.command_done:
			break
		else:
			print(data)
			sock.sendall(settings.command_next.encode(settings.encoding))


if __name__ == "__main__":
	main()
