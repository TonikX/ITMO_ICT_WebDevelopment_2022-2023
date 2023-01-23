import socket
import threading

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 9090))
server_sock.listen(5)

clients = dict()


# send message to everyone
def broadcast(message):
    for client in clients:
        client.sendall(message)


# handling a client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            if message.decode("utf-8") == "{}:bye".format(clients[client]):
                broadcast('{} has left'.format(clients.pop(client)).encode("utf-8"))
                client.close()
                break
            broadcast(message)
        except:
            broadcast('{} has left'.format(clients.pop(client)).encode("utf-8"))
            client.close()
            break


def chat():
    while True:
        client_sock, client_addr = server_sock.accept()
        client_sock.sendall('Nick:'.encode("utf-8"))
        nick = client_sock.recv(1024).decode("utf-8")
        clients[client_sock] = nick
        broadcast('{} joined!'.format(nick).encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client_sock,))
        thread.start()


chat()
