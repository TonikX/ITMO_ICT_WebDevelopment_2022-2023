import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 4800))
server.listen()

connects = []
names = []

def print_clients(msg, name = 'Server', ignore = ''):
    for connect in connects:
        if connect != ignore:
            connect.send(f'{name} -> {msg.decode()}'.encode())
        
def handle(conn):
    while True:
        try:
            req_msg = conn.recv(1024)
            print_clients(req_msg, names[connects.index(conn)], conn)
        except:
            i = connects.index(conn)
            connects.remove(conn)
            conn.close()
            nickname = names[i]
            print_clients(f'{nickname} left!'.encode())
            names.remove(nickname)
            break
        
def receive():
    while True:
        conn, addr = server.accept()

        conn.send('reg'.encode())
        name = conn.recv(1024).decode()
        names.append(name)
        connects.append(conn)
        conn.send('Connected to server!\n'.encode())
        print_clients(f"{name} joined!".encode())
        th = threading.Thread(target=handle, args=(conn,))
        th.start()

receive()