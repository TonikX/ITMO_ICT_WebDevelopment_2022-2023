import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 2465))
user = input("Enter your nickname: ")


def receiving_message():
    while True:
        message = client.recv(8192)
        message = message.decode("utf-8")
        if message == "Whats your name?":
            client.sendto(user.encode("utf-8"), ("127.0.0.1", 2467))
        else:
            print(message)


def sending_message():
    while True:
        text = input("")
        message = f"{user}: {text}"
        client.sendto(message.encode("utf-8"), ("127.0.0.1", 2467))


receive_thread = threading.Thread(target=receiving_message)
sending_thread = threading.Thread(target=sending_message)
receive_thread.start()
sending_thread.start()