import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 9090
sock.bind((host, port))
sock.setblocking(False)

print("Сервер запущен", host, port)

sock.listen(3)

while True:
    try:
        clientsocket, (client_host, client_port) = sock.accept()
        print('Got connection from', client_host, client_port)
        data = clientsocket.recv(16384)
        HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
        body = """
            <html>
            <body>
            <h1>Hello world!</h1>
            </body>
            </html>
        """
        response = HDRS + body
        clientsocket.send(response.encode('utf-8'))
        clientsocket.close()
        break
    except socket.error:
        print("Жду")
        time.sleep(3)
    except KeyboardInterrupt:
        clientsocket.close()