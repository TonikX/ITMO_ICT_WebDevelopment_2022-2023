import socket
from _thread import *

LOCAL_PORT = 25030
MAX_CLIENTS = 10
BUFFER_SIZE = 1024

sock = socket.socket()
sock.bind(('', LOCAL_PORT))
sock.listen(MAX_CLIENTS)

list_of_users = []  # список пользователей


def client_thread(user):  # функция получения и обработки сообщений пользователя
    connection = user[0]
    connection.send('Добро пожаловать в чат!'.encode('utf-8'))

    while True:
        try:
            name = user[1]
            data = connection.recv(1024)
            if data:
                message = data.decode('utf-8')
                if name == '':  # если имя не присвоено, присваимваем
                    user[1] = message
                    print('Новый пользователь: ' + message)
                    broadcast(message + ', добро пожаловать в чат!', connection)
                else:
                    message_to_send = name + ': ' + message
                    broadcast(message_to_send, connection)

            else:
                if user in list_of_users:
                    list_of_users.remove(user)
        except:
            continue


def broadcast(message, connection):  # функция рассылки сообщения всем пользователям чата, кроме выбранного
    for user in list_of_users:
        user_conn = user[0]
        if user_conn != connection:
            try:
                user_conn.send(message.encode('utf-8'))
            except:
                if user in list_of_users:
                    list_of_users.remove(user)


while True:  # в бесконечном цикле принимаем новые подключения и создаем на каждое отдельный поток
    conn, addr = sock.accept()
    list_of_users.append([conn, ''])
    print(addr[0] + " connected")
    start_new_thread(client_thread, (list_of_users[len(list_of_users) - 1],))

sock.close()
