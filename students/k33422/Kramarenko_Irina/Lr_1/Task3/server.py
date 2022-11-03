import socket

host = 'localhost'
port = 9090
addr = (host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(1)
sock, client_addr = sock.accept()
sock.recv(1024)

response_type = "HTTP/1.1 200 OK\n"
headers = "Content-Type: text/html\n\n"
body = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<form action="">
Имя: <input type="text" name="name"><br>
Фамилия: <input type="text" name="surname"><br>
Введите логин: <input type="text" name="login">
</form>
</body>
</html>
"""
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
sock.close()