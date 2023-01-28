import socket
import threading

host = 'localhost'
port = 5002
addr = (host, port)

clients = []  # массив с адресами
nicknames = []  # массив с именами
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen()


def broadcast(message): #отправляем сообщения всем подключенным
    for client in clients:
        client.send(message)


def handle(client): #обращаемся к сообщениям клиентов
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('utf-8'))
            nicknames.remove(nickname)
            break


def receive():
    while True:
        client, address = sock.accept()
        print("Connected with {}".format(str(address)))

        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('utf-8'))
        client.send('Connected to server!'.encode('utf-8'))

#обращение к потоку клиента
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()
