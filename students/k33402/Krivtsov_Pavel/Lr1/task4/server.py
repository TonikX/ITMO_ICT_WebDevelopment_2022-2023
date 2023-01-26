import socket
import threading
import typing as tp


class User:
    def __init__(self, name: str, sock: socket.socket):
        self.name = name
        self.sock = sock


class ChatServer:
    def __init__(self):
        self.alive = True
        self.sock = self.__create_tcp_socket()
        self.users: tp.List[User] = []

    def __create_tcp_socket(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((socket.gethostname(), 1234))
        sock.listen()

        return sock

    def __send_data_to_user(self, user_socket: socket.socket, data: str):
        try:
            user_socket.send(data.encode())
        except:
            pass

    def __get_data_from_user(self, user_socket: socket.socket) -> str:
        data = ""
        try:
            data = user_socket.recv(1024).decode()
        finally:
            return data

    def __remove_user_from_chat(self, user: User):
        user.sock.close()
        self.users.remove(user)
        self.send_broadcast_message(None, f'{user.name} has left the chat')

    def switch_off(self):
        self.alive = False
        for user in self.users:
            self.__send_data_to_user(user.sock, "!END")
            user.sock.close()
        self.sock.close()

    def send_broadcast_message(self, author: tp.Optional[str], text: str):
        if author is None:
            data = f"{text}"
        else:
            data = f"{author}: {text}"

        for user in self.users:
            self.__send_data_to_user(user.sock, data)

    def handle_connection(self, user: User):
        try:
            while self.alive:
                message = self.__get_data_from_user(user.sock)
                if message != "!QUIT":
                    self.send_broadcast_message(user.name, message)
                else:
                    break
        finally:
            self.__remove_user_from_chat(user)

    def serve_forever(self):
        while self.alive:
            user_socket, _ = self.sock.accept()

            self.__send_data_to_user(user_socket, "Enter Username")
            username = self.__get_data_from_user(user_socket)

            user = User(username, user_socket)
            self.users.append(user)
            self.send_broadcast_message(None, f"{username} has connected to the chat")

            thread = threading.Thread(target=self.handle_connection, args=(user,))
            thread.start()

    def start(self):
        try:
            self.serve_forever()
        except KeyboardInterrupt:
            self.switch_off()


if __name__ == "__main__":
    ChatServer().start()
