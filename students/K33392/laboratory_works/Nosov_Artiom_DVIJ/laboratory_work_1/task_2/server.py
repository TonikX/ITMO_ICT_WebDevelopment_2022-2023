# Поиск площади параллелограмма.

import socket
# Создаем сокет (конечную точку для обмена данными) с использованием протокола TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем сокет к текущему хосту (компьютеру) и порту 7070
s.bind((socket.gethostname(), 7070))
# Начинаем прослушивать (слушать) входящие соединения, позволяя до 10 клиентских соединений в очереди
s.listen(10)
# Запускаем бесконечный цикл для ожидания и обработки входящих клиентских соединений
while True:
    # Принимаем входящее клиентское соединение и получаем объект клиентского соксета (clsocket)
    # и адрес клиента (address)
    clsocket, address = s.accept()
    # Получаем данные (строку) от клиента (передаем допустимую длину сообщения в recv)
    data = clsocket.recv(1000)
    # Декодируем полученные данные в строку и разделяем их на два значения, a и h
    a, h = data.decode().split()
    S = str(float(a) * float(h))
    # Отправляем результат обратно клиенту в виде байтовой строки
    clsocket.send(bytes(S, 'utf-8'))
    # Закрываем клиентский соксет
    clsocket.close()
