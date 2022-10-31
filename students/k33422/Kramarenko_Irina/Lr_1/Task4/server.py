import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9090))
print("Сервер подключен")
server.listen(10)

clients = []
end = []


def accept():
    while True:
        client, addr = server.accept()
        clients.append(client)


def recv(client):
    while True:
        try:
            rcvd = client.recv(1024)
        except Exception as e:
            clients.remove(client)
            end.remove(client)
            break
        print(rcvd.decode("utf-8"))
        for cl in clients:
            if cl != client:
                cl.send(rcvd)


def send():
    while True:
        print("")
        to_send = input("")
        print()
        if to_send == "exit":
            break
        print("Отправить: %s"% to_send)
        for client in clients:
            client.send(f"Сервер: {to_send}".encode("utf-8"))


def threads():
    while True:
        for cl in clients:
            if cl in end:
                continue
            index = threading.Thread(target=recv, args=(cl,))
            index.start()
            end.append(cl)


thread1 = threading.Thread(target=threads, name="input")
thread1.start()

thread2 = threading.Thread(target=send, name="out")
thread2.start()

thread3 = threading.Thread(target=accept, name="accept")
thread3.start()

thread2.join()

for client in clients:
    client.close()
print("Сервер отключен")