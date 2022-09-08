import socket


with socket.socket() as s:
    s.bind(('', 8080))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        with open('res/index.html') as fin:
            massage = fin.read()
        response = 'HTTP/1.0 200 OK\n\n' + massage
        conn.sendall(response.encode('utf-8'))
