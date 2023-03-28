import socket
import threading

HOST = '127.0.0.1' #локальный хост
PORT = 55555 #порт

username = input("Введите имя: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание сокета
client.connect((HOST, PORT)) #подключение к хосту и порту

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'Введите имя':
                client.send(username.encode('utf-8'))
            else:
                print(message)
        except:
            print("Ошибка подключения к серверу!")
            client.close()
            break

def write():
    while True:
        message = f'{username}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()