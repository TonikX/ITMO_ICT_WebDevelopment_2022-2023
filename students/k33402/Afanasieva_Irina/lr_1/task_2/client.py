# Variant a. - теорема пифагора
import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(("127.0.0.1", 12400))

# Два прохода цикла, тк 2 вводных числа
for _ in range(2):
    print(my_socket.recv(16384).decode())  # Сообщение от сервера
    inp = input(">> ")  # Вводимые катеты
    my_socket.send(inp.encode())  # Отправка на сервер

print(my_socket.recv(16384).decode())
my_socket.close()
