import socket


with socket.socket() as s:
    s.bind(('', 8080))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        with open('C:/Users/krish/Учеба/5 семестр/Web-разработка/ITMO_ICT_WebDevelopment_2022-2023/students/k33401/Chernov_Egor/Lr1/res/index.html') as fin:
            message = fin.read()
        print(conn.recv(16348).decode('utf-8'))
        response = 'HTTP/1.0 200 OK\n\n' + message
        conn.sendall(response.encode('utf-8'))
