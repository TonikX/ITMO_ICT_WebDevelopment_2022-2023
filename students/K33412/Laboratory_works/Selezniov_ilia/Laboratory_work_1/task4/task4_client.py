import socket
import threading
from string import ascii_letters, digits

from secrets import choice


HOST, PORT = "localhost", 9999


def receive_messages(token: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        connect_msg = "Kind: receiver\nToken: " + token + "\n"
        sock.sendall(bytes(connect_msg, "utf-8"))
        while True:
            received = sock.recv(1024)
            if received:
                print("Received message: " + str(received, "utf-8"))


def send_messages(token: str) -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        connect_msg = "Kind: sender\nToken: " + token + "\n"
        sock.sendall(bytes(connect_msg, "utf-8"))
        while True:
            inp = input()
            sock.sendall(bytes(inp, "utf-8"))


if __name__ == "__main__":
    print("To send a message, type it into the terminal and press enter")
    token = ''.join(choice(
            ascii_letters + digits
    ) for _ in range(16))
    recv = threading.Thread(target=receive_messages, args=(token,))
    recv.start()
    send = threading.Thread(target=send_messages, args=(token,))
    send.start()
