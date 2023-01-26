import socket
import threading

host = "localhost"
port = 2465
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("The chat has been started!")

clients = []
users = []


def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)


def handle(client):
    while True:
        message = client.recv(8192)
        broadcast(message, client)


def receive():
    while True:
        connection, address = server.accept()
        message = "What's your username?"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192).decode("utf-8")
        users.append(user)
        clients.append(connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()