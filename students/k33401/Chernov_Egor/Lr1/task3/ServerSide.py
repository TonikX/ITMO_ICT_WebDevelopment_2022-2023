import socket
import os


with socket.socket() as s:
    s.bind(('', 8080))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        work_path = os.getcwd()
        res_path = ('\\'.join(work_path.split('\\')[:-1]) + '\\res\\index.html').replace('\\', '/')
        with open(res_path) as fin:
            message = fin.read()
        print(conn.recv(16348).decode('utf-8'))
        response = 'HTTP/1.0 200 OK\n\n' + message
        conn.sendall(response.encode('utf-8'))
