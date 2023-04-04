import socket
from threading import Thread

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
server.bind(('127.0.0.1', 9090))
server.listen(10)

users = []

# отправляем новое сообщение всем юзерам
def send_all(mes):
    for user in users:
        user.send(mes)

# случшаем юзеров
def user_listen(user):
    print(users)
    print('user listen')
    while True:
        data = user.recv(2048)  # не раскодируем байты, так как их будем дальше отправлять
        if not data:
            # Клиент отключился
            break
        send_all(data)


# запуск сервера и добавление юзеров
def start_server():
    while True:
        user_sock, addr = server.accept()  # блокирующий поток
        print(f'User<{addr[0]}> con')

        users.append(user_sock)
        user_thread = Thread(target=user_listen,
                             args=[user_sock])  # запятая - показывает питону, что список неизменяемый
        user_thread.start()  # запуск потока



if __name__ == '__main__':
    start_server()