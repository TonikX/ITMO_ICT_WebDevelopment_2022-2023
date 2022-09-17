import socket
import threading


def accept():
    while 1:
        try:
            conn, addr = s.accept()
            print(f"New user {conn.getpeername()[1]} was added")
            conn.send(b"...Write \"/exit\" for live this chat...\n")
            message = f"...New member: {addr[1]}...\n"
            for user in users:
                user.send(message.encode('utf-8'))
            users.append(conn)
            # Start a thread which receives messages
            t_in = threading.Thread(target=in_data, name='in', args=(conn,))
            t_in.start()
        except socket.error:
            break


def in_data(t_conn):
    t_user = t_conn.getpeername()[1]
    while 1:
        try:
            data = t_conn.recv(1024)
            decode_data = data.decode('utf-8')
            # Start a thread which sends messages
            t_out = threading.Thread(target=out_data, name='out', args=(t_conn, decode_data, ), daemon=True)
            t_out.start()
            t_out.join()
        except socket.error:
            print(f"User {t_user} left")
            break


def out_data(t_conn, message):
    t_user = t_conn.getpeername()[1]
    if message == '/exit':
        users.remove(t_conn)
        specific_message = f"...User {t_user} left...\n".encode('utf-8')
        t_conn.close()
    else:
        specific_message = f"User {t_user}: {message}".encode('utf-8')
    for user in users:
        if user == t_conn:
            continue
        user.send(specific_message)


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = ''
        port = 8080
        s.bind((host, port))
        s.listen(5)
        users = []
        print('Chat\'s started')
        # Start a thread which accepts sockets
        t_accept = threading.Thread(target=accept, name='accept', daemon=True)
        t_accept.start()
        while 1:
            # Checking server shutdown
            check = input('Write \"/terminate\" to stop this chat\n')
            if check == '/terminate':
                s.close()
                print('Chat\' stopped')
                break
