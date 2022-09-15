import socket
import threading


def in_data(t_conn):
    t_user = str(t_conn.getpeername()[1])
    while 1:
        try:
            data = t_conn.recv(16384)
            decode_data = data.decode('utf-8')
            if decode_data == '/exit':
                users.remove(t_conn)
                for user in users:
                    user.send(f"...User {t_user} left...\n".encode('utf-8'))
                t_conn.close()
                if len(users) == 0:
                    s.close()
                break
            for user in users:
                if user == t_conn:
                    continue
                user.send(('User ' + t_user + ': ' + decode_data).encode('utf-8'))
        except socket.error:
            print("Error in in_data()")
            print(len(users))
            break


if __name__ == "__main__":
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        host = ''
        port = 8080
        s.bind((host, port))
        s.listen(5)
        users = []
        print('Chat\'s started')
        while 1:
            try:
                conn, addr = s.accept()
                conn.send(b"...Write \"/exit\" for live this chat...\n")
                message = f"...New member: {addr[1]}...\n"
                for user in users:
                    user.send(message.encode('utf-8'))
                users.append(conn)
                t = threading.Thread(target=in_data, name='in', args=(conn,))
                t.start()
            except socket.error:
                print('Chat\' stopped')
                break
