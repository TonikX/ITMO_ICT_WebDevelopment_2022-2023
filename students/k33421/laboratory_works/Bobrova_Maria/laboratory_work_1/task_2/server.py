import socket


def pifagor(a, b): #функия, которая возвращает гипотенузу
    return a**2 + b**2


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание сокета для сервера TCP
sock.bind((socket.gethostname(), 1234))
# Для привязки используется функция bind сокета, которая принимает массив, содержащий два элемента: хост и порт.
sock.listen(1) #максимальное число соединений
#Ф-ция ждёт появление входящего соединения и возвращает связанный с ним сокет и адрес подключившегося.
#Адрес — массив, состоящий из IP-адреса и порта.
conn, addr = sock.accept()
#отправка данных в закодированном виде, т.к. ф-ция send принимает тип bytes
conn.send(str.encode(f"Hello, client\n"
                     f"I solve Pythagorean theorem\n"
                     f"Enter A as a number\n"))
a = "" #катет
b = "" #катет
c = "" #гипотенуза

while not c:
    while not a: #первый катет
        data = conn.recv(1024).decode() #чтение данных с определенным кол-м байт
        if data.isdigit(): #если данные числовые
            a = int(data) #перевод в тип данных integer
            conn.send(b"Enter B as a number\n") #сообщение появляется в терминале
        else:
            conn.send(b"Not a number\n" 
                      b"Enter A as a number\n") #сообщение появляется в терминале, если данные не числовые

    while not b: #второй катет
        data = conn.recv(1024).decode()
        if data.isdigit():
            b = int(data)
        else:
            conn.send(b"Not a number\n"
                      b"Enter B as a number\n")

    c = pifagor(a, b) #функция принимает два введенных числа и считает гипотенузу
    conn.send(str.encode(f"Ответ: {c}")) #отправка ответа

conn.close() #закрытие сокета
