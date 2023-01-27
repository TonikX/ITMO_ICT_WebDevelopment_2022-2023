import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
conn, addr = sock.accept()
print('connected with:', addr)

with open('index.html') as f:
    page = f.read()
response = 'HTTP/1.0 200 OK\n\n' + "Content-Type: text/html\n\n" + page
conn.sendall(response.encode("utf-8"))

conn.close()