import socket

port = 8888
host = "localhost"

sock = socket.socket()
sock.bind((host, port))

sock.listen(10)
sock, addr = sock.accept()
sock.recv(1024)

response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
page = open('index.html','r')
body = page.read()
resp = response_type + headers + body
sock.send(resp.encode("utf-8"))
page.close()
sock.close()