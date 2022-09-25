import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 8080)) #подключение к серверу

num = input("Enter a, b, c: \n") #ввод данных
client.send(num.encode("utf-8")) #отправка байтовой строки
data = client.recv(1024).decode("utf-8") #получение данных и декодирование байт-строки
print("result: ", data) #вывод данных
client.close()