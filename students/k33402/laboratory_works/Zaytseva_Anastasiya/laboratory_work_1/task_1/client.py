import socket

HELLO_MESSAGE = 'Hello, server'
LOCAL_PORT = 25030
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # создание UDP сокета
sock.sendto(HELLO_MESSAGE.encode("utf-8"), ("localhost", LOCAL_PORT))  # отправляем сообщение по адресу сервера
data = sock.recv(BUFFER_SIZE)  # получаем ответное сообщение
print(data.decode("utf-8"))  # выводим ответное сообщение
