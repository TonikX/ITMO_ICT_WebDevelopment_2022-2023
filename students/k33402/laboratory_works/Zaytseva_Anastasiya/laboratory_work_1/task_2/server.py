import socket
from math import sqrt

LOCAL_PORT = 25030
MAX_CLIENTS = 1
BUFFER_SIZE = 1024

sock = socket.socket()  # создание TCP сокета
sock.bind(('', LOCAL_PORT))  # привязка сокета к локальному порту
sock.listen(MAX_CLIENTS)  # установка ограничения на максимальное число подключенных клиентов
conn, addr = sock.accept()  # принимаем подключение 1 клиента
print('Соединение установлено.')

step = 1
with_hypo_input = False
side_a = 0
side_b = 0


def solve_pyth(a, b, with_hypo):  # функция для нахождения стороны треугольника по теореме Пифагора
    high = a if a > b else b
    low = a if a < b else b
    return sqrt(high * high + low * low * (-1 if with_hypo else 1))


while True:  # в бесконечном цикле
    data = conn.recv(1024)  # получаем сообщение клиента
    if not data:
        break
    message = data.decode('utf-8')

    if message == 'завершить':  # завершаем работу по команде клиента
        break
    if step == 1:  # в зависимости от текущего шага алгоритма, запрашиваем у клиента данные
        conn.send('Вы собираетесь вводить гипотенузу? (да/нет)'.encode('utf-8'))
        print('Отправлен вопрос про гипотенузу.')
        step += 1
    elif step == 2:
        if message.lower() == 'да':
            with_hypo_input = True
        print('Получен ответ: ' + message)
        conn.send('Пожалуйста, введите первую сторону.'.encode('utf-8'))
        print('Отправлен запрос первой стороны.')
        step += 1
    elif step == 3:
        side_a = float(message)
        print('Получен ответ: ' + message)
        conn.send('Пожалуйста, введите вторую сторону.'.encode('utf-8'))
        print('Отправлен запрос второй стороны.')
        step += 1
    elif step == 4:
        print('Получен ответ: ' + message)
        side_b = float(message)
        side_c = solve_pyth(side_a, side_b, with_hypo_input)
        print('Отправлено решение: ' + str(side_c))
        conn.send(('Третья сторона: ' + str(side_c)).encode('utf-8'))
        step = 1

conn.close()
