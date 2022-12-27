import socket
from threading import Thread


def send_message():
    while True:
        text = input()
        sock.sendall(bytes(text, "utf-8"))
        if text == "q":
            sock.close()
            break


def receive_message():
    try:
        while True:
            data = sock.recv(1024)
            udata = data.decode("utf-8")
            print(udata)
    except ConnectionAbortedError:
        print('You left the chat')



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 8080))
send_thread = Thread(target=send_message)
get_thread = Thread(target=receive_message)

send_thread.start()
get_thread.start()
