# Импортируем библиотеку socket  
import socket
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Подключаемся к другому хосту
s.connect((socket.gethostname(), 2222))

while True:

    cat = input("Введите катеты через пробел: ")
# Случай завершения сеанса 
    if cat == "over":
        break
# Отправляем строку, используя кодировку 
    s.send(cat.encode('utf8'))
# Получаем данные порциями по 1024 байта
    answer = s.recv(1024)
# Выводим результат, преобразовывая полученные байты в строковый объект
    print("Гипотенуза равна "+answer.decode('utf8'))
    print("Напишите 'over' для завершения сеанса")
s.close()