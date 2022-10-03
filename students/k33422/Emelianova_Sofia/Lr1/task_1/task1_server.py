# Импортируем библиотеку socket  
import socket 
# Выбираем сообщение клиенту
mfs = "Hello, client" 
# Кодируем строку
data = str.encode(mfs) 
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
#  Связываем сокет с хостом и портом
s.bind((socket.gethostname(), 2222)) 
 
while True: 
# Получаем данные порциями по 1024 байта
    mes = s.recvfrom(1024) 
# Делим сообщение по индексам 
    message = mes[0] 
    address = mes[1] 
     
    print(message) 
# Отправляем ответ клиенту 
    s.sendto(data, address)