import socket
with socket.socket() as sock:
    sock.bind((socket.gethostname(), 1234))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        with open('C:/Users/work11pro1/.virtualenvs/ITMO_ICT_WebDevelopment_2022-2023/students/k33421/laboratory_works/Bobrova_Maria/laboratory_work_1/task_3/index.html') as f:
          msg = f.read()
        print(conn.recv(16348).decode('utf-8'))
        response = 'HTTP/1.0 200 OK\n\n' + msg
        conn.sendall(response.encode('utf-8'))
