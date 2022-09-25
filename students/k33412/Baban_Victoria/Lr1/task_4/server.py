import socket
import threading

def send_message(sock, msg):
    for client in clients:
        if sock != client:
            client.send(msg)

def handle_client(socket, address, username):
    if not clients.setdefault(socket):
        clients[socket] = username
        print(f'{username}[{address[0]}:{address[1]}] присоединился к чату')
        send_message(socket, f'Пользователь {username} присоединился к чату'.encode())

    while True:
        try:
            message = socket.recv(1024)
            if message.decode('utf-8').find('EXIT FROM CHAT') != -1:
                print(f'{username}[{address[0]}:{address[1]}] покинул чат')
                send_message(socket, f'Пользователь {username} покинул чат'.encode())
                clients.pop(socket)
                break
            send_message(socket, message)
        except ConnectionResetError:
            print(f'{username}[{address[0]}:{address[1]}] неожиданно пропал...')
            send_message(socket, f'Пользователь {username} неожиданно пропал...'.encode())
            break
    socket.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
clients = {}

while True:
  try:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode('utf-8')
    t1 = threading.Thread(target=handle_client, args=(conn, addr, data))
    t1.start()
  except KeyboardInterrupt:
    print('Server stopped')
    break

conn.close()
