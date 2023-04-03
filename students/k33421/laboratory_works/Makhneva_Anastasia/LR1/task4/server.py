import socket
import threading

host = "localhost"
port = 2468
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print("the chat is up")

clients = []
users = []


def broadcast(message, client):
    for i in clients:
        if i != client:
            i.send(message)


def handle(client):
    while True:
        message = client.recv(8192)
        if message.decode("utf-8") == "leave":
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
        connection, address = server.accept()
        message = "please enter your username"
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192)
        user = user.decode("utf-8")
        users.append(user)
        clients.append(connection)
        message = "you have successfully entered the chat"
        connection.sendto(message.encode("utf-8"), address)
        message = "type 'exit' to leave the chat"
        connection.sendto(message.encode("utf-8"), address)
        message = "{} has entered the chat".format(user)
        broadcast(message.encode("utf-8"), connection)
        thread = threading.Thread(target=handle, args=(connection, ))
        thread.start()


receive()
