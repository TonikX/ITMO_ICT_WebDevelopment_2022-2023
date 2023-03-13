import socket
import threading

class Server():
    def __init__(self):
        self.user_list = []
        self.sock = socket.socket()
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('localhost', 5678))
        self.sock.listen(5)
        print('Server started')

    def run(self):
        try:
            while True:
                client_sock, addr = self.sock.accept()
                self.user_list.append(client_sock)
                threading.Thread(target=self.check_messages, args=(client_sock,)).start()
        except KeyboardInterrupt:
            self.user_list = []
            self.sock.close()

    def check_messages(self, client_sock):
        try:
            while True:
                msg = client_sock.recv(1024).decode()
                if msg:
                    self.show_msg(client_sock, msg)
        except Exception:
            self.terminate_connection(client_sock)

    def terminate_connection(self, client_sock):
        self.user_list.remove(client_sock)

    def show_msg(self, client_sock, msg):
        print(msg)
        for user in self.user_list:
            if user != client_sock:
                user.sendall(msg.encode())

if __name__=='__main__':
    server = Server()
    main_thread = server.run()
