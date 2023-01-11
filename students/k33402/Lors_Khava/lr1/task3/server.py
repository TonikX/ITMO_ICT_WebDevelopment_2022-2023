import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080))
server.listen(10)

while True:
    try:
        clientsocket, address = server.accept()
        html_p = open('index.html')
        html_content = html_p.read()
        html_p.close()

        html_resp = 'HTTP/1.0 200 OK\n' + html_content 

        clientsocket.sendall(html_resp.encode('utf-8'))
        clientsocket.close()
        
    except KeyboardInterrupt: 
        server.close() 
        break
