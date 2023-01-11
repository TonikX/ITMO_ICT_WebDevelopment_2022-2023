import socket
import threading
import datetime

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.connect(("127.0.0.1", 8081))

def send_mes():
    while True:
        message = input()
        conn.send(message.encode("utf-8"))

def get_m():
    while True:
        message = conn.recv(16384).decode("utf-8")
        print(str(datetime.datetime.now()) + ": " + message)

print("Hello! Write your message:")

thread_send = threading.Thread(target=send_mes, args=())
thread_get = threading.Thread(target=get_m, args=())

thread_send.start()
thread_get.start()


