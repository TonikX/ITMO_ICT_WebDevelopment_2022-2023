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
