import socket
import threading

server = socket.socket()
server.bind(('127.0.0.1', 8888))
server.listen()

clients = []


def client_thread(client):
    while True:
        msg = client.recv(1024)
        mail_all(msg, client)


def mail_all(msg, current_client):
    for client in clients:
        client.send(msg)


while True:
    client, addr = server.accept()
    print(f'Новый клиент по адресу {addr}')
    client.send('Connected to server!'.encode('utf-8'))

    clients.append(client)

    threading.Thread(target=client_thread, args=(client,)).start()