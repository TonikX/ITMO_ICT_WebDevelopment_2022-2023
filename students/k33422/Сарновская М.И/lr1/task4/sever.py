
import socket
import threading

HOST = '127.0.0.1' #локальный хост
PORT = 55555 #порт

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание сокета
server.bind((HOST, PORT)) #связываем с хостом и портом

clients = [] #для хранения подключенных клиентов
usernames = [] #для хранения имен подключенных клиентов

def broadcast(message):
    for client in clients:
        client.send(message) #отправляем сообщение каждому клиенту

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} покинул чат!'.encode('utf-8'))
            usernames.remove(username)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Подключен: {str(address)}")

        client.send('Введите имя'.encode('utf-8'))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"Имя пользователя: {username}")
        broadcast(f'{username} присоединился к чату!'.encode('utf-8'))
        client.send('Вы подключены к чату!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Сервер запущен!")
server.listen()
receive()