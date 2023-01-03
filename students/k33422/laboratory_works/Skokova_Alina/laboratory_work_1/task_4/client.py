import socket
import threading

def send_msg():
    while True:
        msg = input()
        client.send(msg.encode('utf-8'))

def get_msg():
    while True:
        msg = client.recv(1024)
        print(msg.decode('utf-8'))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9095))

thread_sending = threading.Thread(target=send_msg)
thread_sending.start()

thread_getting = threading.Thread(target=get_msg)
thread_getting.start()