import socket
import threading

# Choosing nickname
nickname = input("Choose your nickname: ")

# Connecting to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080)) # открытие сокета

# Получение данных с сервера 
def receive():
    while True:
        try:
            # получение сообщения от сервера
            message = client.recv(1024).decode('ascii') # получение данных и декодирование байт-строки
            if message == 'NICK': #если получаем сообщения от сервера 'NICK'
                client.send(nickname.encode('ascii')) # то отправляем его свой ник
            else:
                print(message)
        except:
            # закрываем соединение в случае ошибки
            print("An error occured!")
            client.close()
            break

# Отправка сообщений на сервер
def write():
    while True:
        message = '{}: {}'.format(nickname, input('')) # ввод от клиента сообщения и объединение с ником
        client.send(message.encode('ascii')) # отправка сообщения на сервер

# Запуск потоков для прослушивания и записи 
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()