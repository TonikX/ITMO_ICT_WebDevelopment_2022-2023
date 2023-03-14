import socket, threading
from queue import Queue

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 4851))
sock.listen()
users: dict = {}


def send_message(message: str):
    for conn in users:
        author = message.split(" ")[0]
        if author != users[conn]:
            conn.send(message.encode())


def save_user(conn: socket.socket):
    conn.send(b'Enter your name:')
    token = conn.recv(2048).decode("utf-8")
    users[conn] = token
    send_message(f"{token} присоедился к чату!")

    while True:
        message = conn.recv(24000)
        print(f'{token} отправил сообщение: {message.decode("utf-8")}')
        if not message or message == '.q':
            break
        send_message(f'{token} сообщил: {message.decode("utf-8")}')


try:
    while True:
        conn, addr = sock.accept()
        print(f"{conn}, {addr} присоединился к чату")
        thread_user = threading.Thread(target=save_user, args=[conn]).start()
except KeyboardInterrupt:
    print('Stop')
finally:
    sock.close()