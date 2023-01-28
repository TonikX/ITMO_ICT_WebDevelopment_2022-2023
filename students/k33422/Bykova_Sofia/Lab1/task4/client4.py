import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 5002))
nickname = input("Введите ваше имя: ")


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'NICK':
                sock.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            sock.close()
            break


def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        sock.send(message.encode('utf-8'))

#потоки подключения сервера и написания
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
