import socket, threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 8080))
sock.listen()

clients = []
users = []


def broadcast(sms, client):
    for each in clients:
        if each != client:
            each.send(sms)


def handle(client):
    while True:
        sms = client.recv(2000)
        broadcast(sms, client)


def receive():
    while True:
        client, addr = sock.accept()
        client.send('username'.encode())
        user = client.recv(2000).decode()
        clients.append(client)
        users.append(user)
        client.send('Пользователь в чате'.encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()