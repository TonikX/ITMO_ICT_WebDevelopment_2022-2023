import socket

HELLO_MESSAGE = 'Hello, client'
LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание UDP сокета
sock.bind(('', LOCAL_PORT))  # привязка сокета к локальному порту

while True:  # в бесконечном цикле
    data, address = sock.recvfrom(BUFFER_SIZE)   # получаем данные и адрес от клиента
    print(data.decode("utf-8"))  # выводим полученные данные
    sock.sendto(HELLO_MESSAGE.encode("utf-8"), address)  # отправляем ответное сообщение по адресу
