import socket
from threading import Thread

host = "127.0.0.1"
port = 560
clients = set()
sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5)

def listen_for_client(cl):
    while True:
        try:
            message = cl.recv(1024).decode()
        except Exception as e:
            print(f"[!] Ошибка: {e}")
            clients.remove(cl)
        else:
            message = message.replace(" ", ": ")
        for client in clients:
            client.send(message.encode())

while True:
    client, address = sock.accept()
    print(f"{address} подключен.")
    clients.add(client)
    thread = Thread(target=listen_for_client, args=(client,))
    thread.daemon = True
    thread.start()