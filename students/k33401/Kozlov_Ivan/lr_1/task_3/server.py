import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
conn.recv(16384)
response_type = "HTTP/1.0 200 OK\n"
headers = "Content-Type: text/html\n\n"
f = open('index.html','r')
body = f.read()
resp = response_type + headers + body
conn.send(resp.encode("utf-8"))
f.close()
conn.close()