import socket
import _thread

LOCAL_PORT = 25030
BUFFER_SIZE = 1024


def handle_messages(connection):
    while True:
        msg = connection.recv(1024)
        if not msg:
            connection.close()
            break
        print(msg.decode('utf-8'))


sock = socket.socket()
print('Представьтесь, пожалуйста:')
name = input()  # считываем имя пользователя

sock.connect(('localhost', LOCAL_PORT))
print('Соединение установлено.')
_thread.start_new_thread(handle_messages, (sock,))  # в отдельном потоке запускам получение сообщений с сервера в
# бесконечном цикле

sock.send(name.encode('utf-8'))

while True:

    message = input()  # считываем сообщения для отправки в чат в бесконечном цикле
    if message == 'exit':  # завершаем выполнение при получении команды "exit"
        break
    sock.send(message.encode('utf-8'))

sock.close()
