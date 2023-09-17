import socket
# Создаем сокет (конечную точку для обмена данными) с использованием протокола TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Привязываем сокет к текущему хосту (компьютеру) и порту 8080
s.bind((socket.gethostname(), 8080))
# Начинаем прослушивать (слушать) входящие соединения, позволяя до 10 клиентских соединений в очереди
s.listen(10)
# Запускаем бесконечный цикл для ожидания и обработки входящих клиентских соединений
while True:
    # Принимаем входящее клиентское соединение и получаем объект клиентского соксета (clsocket)
    # и адрес клиента (addr)
    clsocket, addr = s.accept()

    # Отправляем HTTP-заголовки клиенту, указывая успешный статус и тип содержимого
    clsocket.send(bytes('HTTP/1.1 200 OK\n', 'utf-8'))
    clsocket.send(bytes('Content-Type: text/html; charset=utf-8\n', 'utf-8'))
    clsocket.send(bytes('Content-Length: 150\n', 'utf-8'))
    clsocket.send(bytes('\n', 'utf-8'))
    clsocket.send(bytes('\n', 'utf-8'))

    # Открываем файл 'index.html' в режиме чтения байтов
    file = open('index.html', 'rb')
    # Читаем файл построчно и отправляем его содержимое клиенту
    for line in file:
        clsocket.send(line)

    # Закрываем клиентский соксет
    clsocket.close()

# Закрываем серверный соксет (по идее, эта строка кода никогда не выполнится, так как цикл while бесконечен)
s.close()
