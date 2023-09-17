import socket
# Создаем сокет UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Привязываем сокет к текущему хосту (компьютеру) и порту 9090
s.bind((socket.gethostname(), 9090))
# Запускаем бесконечный цикл для прослушивания и обработки входящих сообщений
while True:
    # Получаем сообщение (msg) и адрес (address) отправителя
    msg, address = s.recvfrom(2148)
    # Декодируем и печатаем полученное сообщение
    print(msg.decode())
    # Отправлем ответное сообщение
    s.sendto(bytes('Hello, client!', 'utf-8'), address)
