import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 333
sock.bind((host, port))
sock.listen(5)

while True:
	client, addr = sock.accept()
	print('Получил подключение от:', addr)
	client.recv(1024)
	resp_type = 'HTTP/1.0 200 OK\n'
	resp_headers = 'Content-Type: text/html\n\n'
	resp_body = """
		<html>
		<body>
		<h1>Hello, client! It's a nice day to die</h1>
		</body>
    </html>
    """
	response = resp_type + resp_headers + resp_body
	client.send(response.encode('utf-8'))
	client.close()
	break
