import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9090))
s.listen(1)

while True:
    conn, addr = s.accept()
    html_page = open('index.html')
    html_content = html_page.read()
    html_page.close()

    html_response = 'HTTP/1.0 200 OK\n' + html_content

    conn.sendall(html_response.encode('utf-8'))
    conn.close()