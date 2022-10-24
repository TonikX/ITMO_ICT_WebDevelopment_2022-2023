import threading
import socket

nickname = input('Enter a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8001))

def recieve_mes():
    while True:
        try:
            message = client.recv(1024).decode()
            if message == "Send a nickname":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print('Error occurred. Disconnect.')
            client.close()
            break

def send_mes():
    while True:
        message = f"{nickname}: {input('')}".encode()
        client.send(message)


thread_recieve = threading.Thread(target=recieve_mes)
thread_recieve.start()
thread_send = threading.Thread(target=send_mes)
thread_send.start()





