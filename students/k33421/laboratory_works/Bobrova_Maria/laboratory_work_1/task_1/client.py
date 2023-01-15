import socket #импорт библиотеки

conn = socket.socket(socket.SOCK_DGRAM) #создание сокета для сервера UDP
conn.connect((socket.gethostname(), 1234)) #подключение к хосту (IP-адрес и порт)
msg = 'Hello, server' #сообщение для сервера
conn.send(msg.encode("utf-8")) #
data = b"" #создание пустой байтовой строки
tmp = conn.recv(16384) #отсюда все как обычно
while tmp:
    data += tmp
    tmp = conn.recv(16384)
print(data.decode("utf-8"))
conn.close()
