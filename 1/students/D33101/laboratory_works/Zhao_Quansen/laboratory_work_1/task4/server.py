import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 4245))
server.listen()

conns = []
names = []

def print_msg(message, name = 'Сервер', conn_not_send = ''):
    for conn in conns:
        if conn != conn_not_send:
            conn.send(f'{name} говорит > {message.decode()}'.encode())
        
def control(conn):
    while True:
        try:
            message = conn.recv(1024)
            print_msg(message, names[conns.index(conn)], conn)
        except:
            index = conns.index(conn)
            conns.remove(conn)
            conn.close()
            nickname = names[index]
            print_msg(f'{nickname} отключился.'.encode())
            names.remove(nickname)
            break
        
def get():
    while True:
        conn, addr = server.accept()

        conn.send('регистрация'.encode())
        name = conn.recv(1024).decode()
        names.append(name)
        conns.append(conn)

        conn.send('Подключился к серверу!\n'.encode())
        print_msg(f"{name} подключился!-->".encode())
        
        thread = threading.Thread(target=control, args=(conn,))
        thread.start()

get()