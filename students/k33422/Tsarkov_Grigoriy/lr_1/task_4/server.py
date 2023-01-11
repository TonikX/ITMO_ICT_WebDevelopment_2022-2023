import threading
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 7070))
sock.listen(10)

clients = []
users = []


def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)


def handle(client):
    while True:
        message = client.recv(8192)
        if message.decode("utf-8") == "quit":
            i = clients.index(client)
            clients.remove(client)
            client.close()
            user = users[i]
            users.remove(user)
            message = "{} left the chat.".format(user).encode("utf-8")
            broadcast(message, client)
            break
        broadcast(message, client)


def receive():
    while True:
        connection, address = sock.accept()
        message = "What's your username?"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192)
        user = user.decode("utf-8")
        users.append(user)
        clients.append(connection)
        message = "You have entered the chat! Welcome!"
        connection.sendto(message.encode("utf-8"), address)
        message = "Type word 'quit' to leave this chat"
        connection.sendto(message.encode("utf-8"), address)
        message = user + " has entered this chat."
        broadcast(message.encode("utf-8"), connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()
