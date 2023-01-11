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
