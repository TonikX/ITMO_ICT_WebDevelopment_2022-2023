import socket

port = 3968
host = socket.gethostbyname("localhost")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.bind((host, port))

sock.listen(10)
sock, addr = sock.accept()
sock.recv(16384)

response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
page = open('index.html','r')
body = page.read()
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
page.close()
sock.close()