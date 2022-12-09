import socket

host = 'localhost'
port = 2222
add = (host, port)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((add))
s.listen(10)

while True: 
    conn, add = s.accept()
    a = "HTTP/1.0 200 OK\n"
    b = "Content-Type: text/html\n\n"
    file = open('index.html', 'r')
    cont = file.read()
    ans = a + b + cont
    conn.sendall(ans.encode("utf-8"))
    conn.close()