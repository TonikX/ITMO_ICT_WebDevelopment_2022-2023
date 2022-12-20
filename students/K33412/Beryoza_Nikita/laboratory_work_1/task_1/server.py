import socket
import time

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(1)
server.setblocking(False)
print("Сервер запущен!")

while True:
    try:
        clientSock, clientAddress = server.accept()
        server.setblocking(True)
        data = clientSock.recv(4096)
        msg = data.decode("utf-8")
        print(msg)
        server.close()
        break
    except socket.error:
        print("Ожидаю")
        time.sleep(1)
    except KeyboardInterrupt:
        server.close()
        break

