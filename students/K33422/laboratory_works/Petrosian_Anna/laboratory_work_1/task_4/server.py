import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 3968))
sock.listen()

interlocuteurs = []
usernames = []


def broadcast(message):
    for sock_int in interlocuteurs:
        sock_int.send(message)


def handle(sock_int):
    while True:
        try:
            message = sock_int.recv(4096)

            if "exit" in message.decode('utf-8'):
                exitclient(sock_int)
                break

            broadcast(message)

        except Exception as e:
            exitclient(sock_int)
            break


def exitclient(sock_int):
    index = interlocuteurs.index(sock_int)
    interlocuteurs.remove(sock_int)
    sock_int.close()
    username = usernames[index]
    broadcast(f'bye, {username}'.encode('utf-8'))
    usernames.remove(username)


def receive():
    while True:
        try:
            sock_int, client_address = sock.accept()
            print(f'connection established {client_address}')

            sock_int.send('NICKNAME'.encode('utf-8'))
            username = sock_int.recv(4096).decode('utf-8')
            interlocuteurs.append(sock_int)
            usernames.append(username)
            broadcast(f'{username} joined'.encode('utf-8'))

            handle_thread = threading.Thread(target=handle, args=(sock_int,))
            handle_thread.start()

        except KeyboardInterrupt:
            print ("server closed")
            sock.close()
            break

        except Exception as e:
            print('Exception:', e)
            broadcast(f'')

receive()
