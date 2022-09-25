import socket
import threading

username = input("your username: ")


interlocuteur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
interlocuteur.connect(('127.0.0.1', 3968))


def receive():
    while True:
        try:
            message = interlocuteur.recv(4096).decode('utf-8')
            if message == 'NICKNAME':
                interlocuteur.send(username.encode('utf-8'))
            else:
                print(message)

        except Exception as e:
            print(e)
            interlocuteur.close()
            break


def send():
    while True:
        message = input()
        interlocuteur.send(f'{username} > {message}'.encode('utf-8'))


send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)
send_thread.start()
recv_thread.start()
