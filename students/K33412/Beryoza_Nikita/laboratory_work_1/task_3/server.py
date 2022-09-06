import socket

LOCALHOST = "127.0.0.1"
PORT = 3000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
response_type = 'HTTP/1.1 200 OK\n'
headers = 'Content/Type: text/html\n'
server.listen(1)
print("Сервер запущен!")

while True:
    client, (clientSock, clientAddress) = server.accept()
    print('Клиент подключился с IP "' + str(clientSock) + ':' + str(clientAddress) + '"')
    while True:
        data = client.recv(4096)
        req = data.decode()
        if req == "989796":
            client.send(
                response_type.encode()
            )
            continue
        elif req == 'exit':
            client.close()
            print("Отключение от клиента")
            break
        elif req == 'index.html':
            f = open('file_test_1.html', 'r')
            body = f.read()
            res = response_type + headers + body
            client.send(res.encode())
        else:
            client.send('Я не понимаю твой запрос'.encode())
    print("Выключение сервера")
    break
server.close()

