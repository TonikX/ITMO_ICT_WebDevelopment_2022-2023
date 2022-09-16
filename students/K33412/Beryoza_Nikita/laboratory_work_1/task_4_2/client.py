import socket
import threading

host = '127.0.0.1'
port = 1234
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))


def sender():
    global server
    while True:
        msg = input("[+] Type your message > ")
        if len(msg) > 0:
            server.send(msg.encode())


def recv():
    while True:
        print(server.recv(1024).decode())


if __name__ == "__main__":
    t = threading.Thread(target=recv)
    t.start()
    sender()

