import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 9090))
sock.listen(1)

while True:
	try: 
		con, addr = sock.accept()
		data = con.recv(9111989)
		dec_data = data.decode("utf-8")
		print(dec_data)
		con.send(b"Hello, client")
	finally:
		sock.close()
		break