# импортируем библиотеку сокет 
import threading
import socket
# создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# подключаемся к хосту
s.connect((socket.gethostname(), 2222))
nick = input('Для возможности переписываться необходим никнэйм. Введите его, пожалуйста: ')
# Получаем сообщения 
def to_get_mes():
    while True:
        mes = s.recv(1024)
        mesget = mes.decode('utf8')
        if mesget == "send_nickname":
            s.send(nick.encode('utf8'))
        else:
            print(mesget)
# Отправляем сообщения 
def to_send_mes():
    while True:
        messend = f"{nick}: {input('')}"
        s.send(messend.encode('utf8'))

# Создаем многопоточность 
get_part = threading.Thread(target=to_get_mes)
send_part = threading.Thread(target=to_send_mes)
# Начинаем много поточность 
get_part.start()
send_part.start()
# Блокируем поток 
# get_part.join()
send_part.join()
s.close()