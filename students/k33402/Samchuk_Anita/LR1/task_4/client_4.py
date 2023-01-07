
import socket
from threading import Thread

server_host = "127.0.0.1"
server_port = 6060
separator_token = "<SEP>"

sock = socket.socket()
print(f"[*] Connecting to {server_host}:{server_port}...")
sock.connect((server_host, server_port))
print("[+] Connected.")
name = input("Enter your name: ")


def listen_for_messages():
    while True:
        message = sock.recv(1024).decode()
        print(message)

t = Thread(target=listen_for_messages)
t.daemon = True
t.start()

while True:
    to_send = input()
    if to_send.lower() == 'q':
        break
    to_send = f"{name}{separator_token}{to_send}"
    sock.send(to_send.encode())

sock.close()
