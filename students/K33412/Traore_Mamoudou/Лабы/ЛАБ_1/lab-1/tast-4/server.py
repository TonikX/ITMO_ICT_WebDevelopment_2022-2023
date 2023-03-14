import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 8080
server.bind((host, port))
server.listen()

clients = []
users = []


def broadcast(msg, client):
    for each in clients:
        if each != client:
            each.send(msg)


def handle(client):
    while True:
        msg = client.recv(2000)
        broadcast(msg, client)


def receive():
    while True:
        client, addr = server.accept()
        client.send('username'.encode())
        user = client.recv(2000).decode()
        clients.append(client)
        users.append(user)
        client.send('Connection established'.encode())
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


receive()