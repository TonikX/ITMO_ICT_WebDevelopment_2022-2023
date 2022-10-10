import socket

conn = socket.socket()
conn.bind(("127.0.0.1", 3300))
conn.listen(1)

while True:
    try:
        clientsocket, address = server.accept()
        html_page = open('index.html')
        html_content = html_page.read()
        html_page.close()

        html_resp = 'HTTP/1.0 200 OK\n' + html_content 

        clientsocket.send(html_resp.encode('utf-8'))
        clientsocket.close()

    except KeyboardInterrupt: 
        conn.close() 
        break