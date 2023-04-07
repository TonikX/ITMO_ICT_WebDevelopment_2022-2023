import socket
import threading


class MyClient:
    def __init__(self, ip, port):
        self.username = ""
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Подулючаем клиентский сокет к серверу
        self.sock.connect((ip, port))

    # Функция отвечающая за получение сообщений
    def receive(self):
        while True:
            try:
                message = self.sock.recv(1024).decode()
                # "Регистрация" пользователя, клиент отправит серверу имя пользователя
                if message == "What is your username?":
                    self.sock.send(self.username.encode())
                else:
                    print(message)
            except:
                print("Error!")
                self.sock.close()
                break
    
    # Функция отвечающая за отправку сообщение
    def send(self):
        while True:
            # Постоянно читаем и отправляем ввод клиента
            message = input()
            self.sock.send(message.encode())

    def start(self):
        self.username = input("Enter your username: ")
        # Запускаем поток, считывающий сообщения от сервера
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()
        # Поток, считывающий ввод
        send_thread = threading.Thread(target=self.send)
        send_thread.start()


if __name__ == "__main__":
    MyClient("127.0.0.1", 9091).start()
