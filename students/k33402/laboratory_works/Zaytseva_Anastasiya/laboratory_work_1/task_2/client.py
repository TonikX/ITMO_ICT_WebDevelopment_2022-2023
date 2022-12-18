import socket

LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket()  # создаем TCP сокет
sock.connect(('localhost', LOCAL_PORT))  # подключаемся к локальному серверу

while True:  # в бесконечном цикле
    message = input()  # считываем ввод пользователя
    if message.lower() == 'exit':  # если введено "exit", завершаем выполнение
        break
    sock.send(message.encode('utf-8'))  # отправляем введенное сообщение
    data = sock.recv(BUFFER_SIZE)  # получаем ответ от сервера
    print(data.decode('utf-8'))  # выводим ответ

sock.close()
