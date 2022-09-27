import socket
import threading

username = input("your username: ")

sock_int = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_int.connect(('127.0.0.1', 3968))


def receive():
    while True:
        try:
            message = sock_int.recv(4096).decode('utf-8')
            if message == 'NICKNAME':
                sock_int.send(username.encode('utf-8'))
            elif username in message:
                print(message.replace(f"{username} >", 'You >', 1))
            else:

                print(message)

        except Exception as e:
            print(e)
            sock_int.close()
            break


def send():
    while True:
        message = input()
        sock_int.send(f'{username} > {message}'.encode('utf-8'))


send_thread = threading.Thread(target=send)
recv_thread = threading.Thread(target=receive)
send_thread.start()
recv_thread.start()
