import socket

from threading import Thread

users = []
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8080))
sock.listen(10)
sock.setblocking(False)


def chat_users():
    while True:
        sock.setblocking(True)
        con, addr = sock.accept()
        sock.setblocking(False)
        con.send(b'Enter your name:  \n')
        name = con.recv(1024)
        con.send(b'You can send messages now. Press q to leave the chat.  \n')
        name = name.decode("utf-8")
        print(name, 'has joined the chat')
        if con not in users:
            users.append((con, name))


def message():
    while True:
        try:
            for user in users:
                text = user[0].recv(1024).decode('utf-8')
                if text == "q":
                    user[0].close()
                    print('{} has left the chat'.format(user[1]))
                else:
                    print(str(user[1]) + ':' + text)
                for send_user in users:
                    if send_user[0] != user[0]:
                        data = f'{user[1]}: ' + text
                        send_user[0].sendall(data.encode('utf8'))
        except socket.error:
            print('No one is in the chat. Waiting for new users...')
            break


user_thread = Thread(target=chat_users)
message_thread = Thread(target=message)

user_thread.start()
message_thread.start()