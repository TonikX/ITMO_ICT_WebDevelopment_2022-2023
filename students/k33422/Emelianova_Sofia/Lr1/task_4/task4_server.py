# Импортируем библиотеку сокет 
import socket
import threading
# Создаем сокет
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Связываем сокет с хостом и портом 
s.bind((socket.gethostname(), 2222))
# Запускаем режим прослушивания 
s.listen()
# Создаем списки 
clients = []
nicks = []

# Передача сообщений 
def broadcast(mes):
    for cli in clients:
        cli.send(mes)

def handle(cli):
    while True:
        try:
            mes = cli.recv(1024)
            broadcast(mes)
# Исключаем пользователей
        except: 
            i = clients.index(cli)
            clients.remove(i)
            broadcast(f"{nicks[i]} покинул(а) чат.".encode('utf8'))
            nicks.remove(i)
            cli.close()
            break
# Присоединение пользователей 
def recieve():
    while True:
        conn, add = s.accept()
        print(f"Подключение с адресом {add}")
        conn.send("send_nickname".encode('utf8'))
        name = conn.recv(1024)
        nicks.append(name)
        clients.append(conn)
        broadcast(f"Пользователь {name} присоединился к чату.".encode('utf8'))
        conn.send("Вы подключились".encode('utf8'))
# Многопоточность 
        part = threading.Thread(target=handle, args=(conn, ))
        part.start()

if __name__ == "__main__":
    recieve()