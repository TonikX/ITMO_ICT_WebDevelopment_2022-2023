# Импортируем библиотеку socket  
import socket 
# Выбираем сообщение серверу 
mfc = "Hello, server" 
# Кодируем строку
data = str.encode(mfc)
# Подключаемся к хосту
sad = (socket.gethostname(), 2222) 
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
# Отправляем данные серверу 
s.sendto(data, sad) 
# Получаем данные порциями по 1024 байта
mfs = s.recvfrom(1024) 
# Выбираем нужную часть полученного сообщения
msg = mfs[0] 
 
print(msg)