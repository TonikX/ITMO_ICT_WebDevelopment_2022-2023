import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9090))
name = input('Enter your name: ')


def send_message():
    try:
        while True:
            msg = input()
            sock.sendall(bytes(name + ": " + msg, "utf-8"))
            if msg == "Пока":
                sock.close()
                break
    except Exception:
        pass


def receive_message():
    try:
        while True:
            data = sock.recv(1024).decode("utf-8")
            if not data:
                break
            print(data)
        sock.close()
    except Exception:
        pass


send = threading.Thread(target=send_message)
receive = threading.Thread(target=receive_message)

send.start()
receive.start()