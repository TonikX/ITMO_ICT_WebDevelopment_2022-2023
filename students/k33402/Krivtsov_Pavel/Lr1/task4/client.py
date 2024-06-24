import socket
import threading


class ChatClient:
    def __init__(self):
        self.username = ""
        self.alive = True
        self.sock = self.__create_tcp_socket()

    def __create_tcp_socket(self) -> socket.socket:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((socket.gethostname(), 1234))

        return sock

    def __send_data_to_server(self, data: str):
        if self.alive:
            self.sock.send(data.encode())

    def __get_data_from_server(self) -> str:
        return self.sock.recv(1024).decode()

    def __left_from_server(self):
        self.alive = False
        self.sock.close()

        print("You have left the chat")

    def receive(self):
        try:
            while self.alive:
                message = self.__get_data_from_server()
                if message == "Enter Username":
                    self.__send_data_to_server(self.username)
                elif message == "!END":
                    print("The server was interrupted")
                    break
                else:
                    print(message)
        finally:
            self.__left_from_server()

    def send(self):
        while self.alive:
            message = input()
            self.__send_data_to_server(message)

            if message == "!QUIT":
                self.alive = False

    def start(self):
        self.username = input("Enter username: ")

        get_thread = threading.Thread(target=self.receive)
        get_thread.start()

        send_thread = threading.Thread(target=self.send)
        send_thread.start()


if __name__ == "__main__":
    ChatClient().start()
