import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 8080)) #открытие сокета
server.listen(10) #открытие очереди на соединение

while True:
    try:
        clientsocket, address = server.accept()
        data = clientsocket.recv(1024).decode("utf-8") #получение данных и декодирование байт-строки
        a, b, c = float(a), float(b), float(c)
        d = (b ** 2) - (4 * a * c)
        if d < 0:
            msg = "No solutions"
            clientsocket.send(msg.encode("utf-8")) #отправка кодированной строки
        elif d == 0:
            x = -b / (2*a)
            clientsocket.send(f"x = {x}".encode("utf-8")) #отправка кодированной строки
        else:
            x1 = (-b-d ** 0.5)/(2*a)
            x2 = (-b+d ** 0.5)/(2*a)
            clientsocket.send(f"x1 = {x1}, x2 = {x2}".encode("utf-8")) #отправка кодированной строки

    except KeyboardInterrupt: #сработает во время прерывания процесса
        server.close() #закрытие сокета
        break
