import socket

# Создаём User Datagram Protocol сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Подключение сокета к локальной машине, порту 9090
s.connect((socket.gethostname(), 9090))

# Отправляем сообщение серверу
s.sendto(bytes('Hello, server!', 'utf-8'), (socket.gethostname(), 9090))
# Получаем ответ от сервера
msg = s.recvfrom(2148)
# печатаем разкодированное сообщение, полученное от сервера
print(msg[0].decode())
# Закрываем сокет
s.close()
