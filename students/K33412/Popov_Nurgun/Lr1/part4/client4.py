import socket
import threading

class Client():
    def __init__(self):
        self.username = input('Enter your username: ')
        self.sock = socket.socket()
        self.sock.connect(('localhost', 5678))
        self.sock.sendall((self.username + ' entered the chat').encode())
        print('You entered the chat as ' + self.username)

    def send_messages(self):
        try:
            while True:
                msg = input()
                if msg == 'quit_chat':
                    print('You exited the chat')
                    self.sock.sendall((self.username + ' exited the chat').encode())
                    self.sock.close()
                self.sock.sendall((self.username + ': ' + msg).encode())
        except Exception:
            pass

    def check_messages(self):
        try:
            while True:
                new_msg = self.sock.recv(1024).decode()
                if new_msg:
                    print(new_msg)
        except Exception:
            pass

if __name__=='__main__':
    client = Client()
    threading.Thread(target=client.check_messages, args=()).start()
    threading.Thread(target=client.send_messages, args=()).start()
