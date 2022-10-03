import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
addr = (host, port)

username = input("Введите свой ник:")
client.connect(addr)
print("Подключение к серверу выполнено")
print("Введите exit, чтобы закрыть соединение с сервером")


def send():
    while True:
        to_send = input("Введите сообщение: ")
        print()
        if to_send == "exit":
            # print("Соединение с сервером закрыто")
            break
        client.send(f"{username}: {to_send}".encode("utf-8"))
        print("%s:%s"% (username, to_send))


def recv():
    while True:
        rcvd = client.recv(1024)
        print("\n" + rcvd.decode("utf-8"))


thread1 = threading.Thread(target=recv, name="input")

thread2 = threading.Thread(target=send, name="out")

thread1.start()
thread2.start()

thread2.join()

print("Соединение с сервером закрыто")
client.close()
