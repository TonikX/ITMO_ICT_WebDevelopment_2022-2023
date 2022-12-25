import socket
import threading


addressPort = ('127.0.0.1', 7070)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addressPort)
user = input("Enter username: ")


def receiving_message():
    while True:
            message = sock.recv(1024)
            message = message.decode("utf-8")
            if message == "What's your username?":
                sock.sendto(user.encode("utf-8"), addressPort)
            else:
                print(message)


def sending_message():
    while True:
        text = input("")
        if text == "quit":
            sock.sendto(text.encode("utf-8"), addressPort)
            print("You left this chat!")
            sock.close()
            break
        else:
            message = user + ': ' + text
            sock.sendto(message.encode("utf-8"), addressPort)


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()
