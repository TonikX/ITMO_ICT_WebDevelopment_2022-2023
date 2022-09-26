import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 3968))
sock.listen()

clients = []
usernames = []


def broadcast(message):
    for interlocuteur in clients:
        interlocuteur.send(message)


def handle(interlocuteur):
    while True:
        message = interlocuteur.recv(4096)
        #broadcast(message)

        if message == b"EXIT":
            interlocuteur.connection.close()
            clients.remove(interlocuteur)
            broadcast(f'{username} left'.encode('utf-8'))
            break
        else:
                broadcast(message)


def receive():
    while True:
        try:
            interlocuteur, client_address = sock.accept()
            print(f'accepted connection from {client_address}')

            interlocuteur.send('NICKNAME'.encode('utf-8'))
            username = interlocuteur.recv(4096).decode('utf-8')
            clients.append(interlocuteur)
            usernames.append(username)
            broadcast(f'{username} joined'.encode('utf-8'))

            handle_thread = threading.Thread(target=handle, args=(interlocuteur,))
            handle_thread.start()

        except Exception as e:
            print('Exception:', e)
            broadcast(f'')


receive()
