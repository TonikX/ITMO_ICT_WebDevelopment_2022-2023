import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 7070))
sock.listen(10)
conn, addr = sock.accept()

while True:
    html_page = open('index.html')
    html_content = html_page.read()
    html_page.close()

    html_response = 'HTTP/1.0 200 OK\n\n' + html_content

    conn.sendall(html_response.encode('utf-8'))
    conn.close()
