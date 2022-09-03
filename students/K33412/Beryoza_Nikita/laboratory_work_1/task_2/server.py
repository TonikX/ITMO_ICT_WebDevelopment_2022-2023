import socket
import time

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(5)
print("Сервер запущен!")

while True:
    try:
        clientSock, clientAddress = server.accept()
        print('Клиент подключился с IP ' + str(clientAddress))
        while True:
            data = clientSock.recv(4096)
            msg = data.decode("utf-8")
            if msg == "989796":
                clientSock.send(
                    "Введите длинны оснований трапеции и высоту трапеции в таком формате 'a b h'\n".encode()
                )
                continue
            req = msg.split()
            res = (int(req[0]) + int(req[1])) * int(req[2]) / 2
            res = str.encode(str(res))
            clientSock.send(res)
            break
        server.close()
        break
    except socket.error:
        print("Ожидаю")
        time.sleep(1)
    except KeyboardInterrupt:
        server.close()
        break

