import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 9090))
sock.listen(10)
users = set()


def connecting_users():
    while True:
        client, address = sock.accept()
        users.add(client)
        print('User connected:' + str(address))
        cl_add = threading.Thread(target=msg, args=[client, address])

        cl_add.start()


def msg(client, address):

    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            print('info:', data)
            if not data:
                break
            for user in users:
                if user == client:
                    continue
                user.sendall(data.encode('utf8'))
        except Exception:
            users.remove(client)

            break
    print('User have closed chat: ' + str(address))
    client.close()


cnx = threading.Thread(target=connecting_users())
cnx.start()




