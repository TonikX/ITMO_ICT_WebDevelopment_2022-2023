# Импортируем библиотеки socket и math
import socket
import math
# Создаем сокет
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#  Связываем сокет с хостом и портом
s.bind((socket.gethostname(), 2222))
# Запускаем режим прослуживания
s.listen(5)
# Принимаем подключение 
con, ad = s.accept()
msg = ''

while True:
# Получать данные будем "порциями" по 1024 байта
    data = con.recv(1024)
# Преобразовываем полученные байты в строковый объект
    msg = data.decode('utf8')
# Случай завершения сеанса
    if msg == 'over':
        print("Сеанс завершен")
        break
# Делим полученные данные по индексам
    result = 0
    cat_list = msg.split()
    cat1 = cat_list[0]
    cat2 = cat_list[1]
# Преобразовываем  строку в число
    num1 = int(cat1)
    num2 = int(cat2)
# Считаем гипотенузу
    if num1 > 0 and num2 > 0:
        result = math.sqrt(num1**2 + num2**2)
 
    print("Результат посчитан и отправлен")
# Преобразовываем результат в строку
    output = str(result)
# Отправляем результат, используя кодировку 
    con.send(output.encode('utf8'))
con.close()