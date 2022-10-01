import socket
import threading

nickname = input("Имя пользователя: ")

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('127.0.0.1', 4245))

def get():
    while True:
        try:
            message = socket.recv(1024).decode()
            if message == 'регистрация':
                socket.send(nickname.encode())
            else:
                print(message)
        except:
            break
        
def send():
    while True:
        msg = input('')
        if msg == 'out':
            socket.close()
            break
        socket.send(msg.encode())

get_thread = threading.Thread(target = get)
get_thread.start()

send_thread = threading.Thread(target = send)
send_thread.start()