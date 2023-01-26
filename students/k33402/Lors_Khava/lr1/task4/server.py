import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080)) # открытие сокета
server.listen(10) # открытие очереди на соединение

# Списки подключенных клиентов и их ников
clients = []
nicknames = []

# Отправка сообщений всем подключенным клиентам
def broadcast(message):
    for client in clients:
        client.send(message)

# Обработка сообщений от клиентов
def handle(client):
    while True:
        try:
            # broadcasting messages
            message = client.recv(1024)
            broadcast(message) # получает сообщение от клиента и рассылает его всем подключенным клиентам
        except:
            # удаление и закрытие клиентов
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break

# Функция получения данных клиента
def receive():
    while True:
        # принимаем подключение
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # запрос и сохранение ника
        client.send('NICK'.encode('ascii')) # у клиента запрашивают никнейм
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # принт ника и сообщение о подключении
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # обработка потока для клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
receive()