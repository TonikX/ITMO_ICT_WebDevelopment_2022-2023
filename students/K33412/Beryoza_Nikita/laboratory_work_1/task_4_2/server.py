import socket
import select
import threading

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()

connections = []
addresses = []

print(f'Сервер запущен на IP {IP}:{PORT}')


def accept_connections():
    global server_socket
    while True:
        new_connection, new_address = server_socket.accept()
        connections.append(new_connection)
        addresses.append(new_address)
        print("[!] Подключение " + str(new_address[0]) + ":" + str(new_address[1]))


def handler(connection):
    while True:
        msg = input("[+] Type your message > ")
        if len(msg) > 0:
            try:
                connection.send(msg.encode())
            except Exception as error:
                print("Невозможно отправить сообщение из-за:\n" + str(error))
        if msg == "back":
            main()
            break


def recv():
    while True:
        for i, x in enumerate(connections):
            try:
                print(x.recv(1024).decode())
            except:
                del connections[i]
                del addresses[i]


def list_connections():
    global connections
    res = ""
    for i, cc in enumerate(connections):
        try:
            cc.send("Новое подключение".encode())
            res = str(addresses[i][0]) + ":" + str(addresses[0][1]) + "\n"
        except Exception as error:
            print(str(error))
            pass
    return res


def main():
    t1 = threading.Thread(target=accept_connections)
    t1.daemon = True
    t2 = threading.Thread(target=recv)
    t1.start()
    t2.start()
    while True:
        req = input("[+] main > ")
        if req == 'list':
            print(list_connections())
        if req[:7] == "select ":
            handler(connections[int(req[8:])])


main()
