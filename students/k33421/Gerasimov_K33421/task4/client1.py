import socket
import threading


host = "localhost"
port = 9090
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
user = input("What's your username? Enter it here, please: ")


def receiving_message():
    while True:
        message = client.recv(8192)
        message = message.decode("utf-8")
        if message == "What's your username?":
            client.sendto(user.encode("utf-8"), (host, port))
        else:
            print(message)


def sending_message():
    while True:
        text = input("")
        if text == "leave":
            client.sendto(text.encode("utf-8"), (host, port))
            print("You left this chat!")
            client.close()
            break
        else:
            message = "{}: {}".format(user, text)
            client.sendto(message.encode("utf-8"), (host, port))


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()
