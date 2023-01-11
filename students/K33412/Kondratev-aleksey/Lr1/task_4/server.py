import socket
from threading import Thread

HOST = "127.0.0.1"
PORT = 9090
clients = []
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)
print(f"Сервер запущен {HOST}:{PORT}")

def listen_for_client(people):
    while True:
        try:
            message = people.recv(1024).decode()
        except Exception as e:
            print(f"[!] Ошибка: {e}")
            clients.pop(people)
        else:
            message = message.replace(" ", ": ")
        for client in clients:
            client.send(message.encode())

while True:
    client, (port, host) = sock.accept()
    print(f"подключен {port}:{host}.")
    clients.append(client)
    thread = Thread(target=listen_for_client, args=(client,))
    thread.daemon = True
    thread.start()