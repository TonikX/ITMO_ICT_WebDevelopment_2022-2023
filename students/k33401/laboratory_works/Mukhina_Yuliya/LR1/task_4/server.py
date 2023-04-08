import socket, threading

HOST = "127.0.0.1"
PORT = 9091


class MyChat:
    def __init__(self, ip, host):
        # Ключ - клиент, значение - имя пользователя
        self.connections: dict[socket.socket, str] = {}
        # Иниализация самого сервера
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Сервер сокета будет привязан к указанном IP адресу и порту (в данном случае localhost и порт 9091)
        self.server.bind((ip, host))
        # Сервер начинает слушать входящие подключения
        self.server.listen()

    # Функция для отправки сообщений подключенным клиентам
    def broadcast(self, message: str, username: str):
        for client in self.connections.keys():
            client.send(f"{username}: {message}".encode())

    # Обработчики сообщений клиентов
    def handle_client(self, client: socket.socket):
        while True:
            username = str(self.connections.get(client))

            try:
                # Получаем сообщение от клиента в виде байтов и преобразуем в строку
                message = client.recv(1024).decode()
                self.broadcast(message, username)
            except:
                # В случае ошибки закрываем соединение с клиентом
                client.close()
                # Удаляем клиент из известных серверу соединений
                self.connections.pop(client)
                # Информируем других
                self.broadcast(f"{username} left...", "Server")
                break

    def receive(self):
        print("It's alive!")

        while True:
            client, address = self.server.accept()
            print(f"{str(address)} connected!")

            # При новом подключении узнаём имя пользователя и сохраняем его
            client.send(b"What is your username?")
            username = client.recv(1024).decode()
            self.connections[client] = username

            # Информируем подключенных клиентов о новом подключении
            self.broadcast(f"{username} joined!", "Server")

            # Создаём поток под новый клиент, чтобы обрабатывать их одновременно
            thread = threading.Thread(target=self.handle_client, args=(client,))
            thread.start()

    def run(self):
        self.receive()


if __name__ == "__main__":
    MyChat(HOST, PORT).run()
