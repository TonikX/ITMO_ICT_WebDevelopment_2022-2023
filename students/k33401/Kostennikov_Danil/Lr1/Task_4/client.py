import socket
import threading

HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

name = input("Enter your name: ")


def receive():
    while True:
        res = s.recv(1024)
        print(res.decode("utf-8"))

def write():
    while True:
        mes = input('')
        s.send(f"{name}: {mes}".encode("utf-8"))
    

thread = threading.Thread(target=write)
thread2 = threading.Thread(target=receive)
thread2.start() , thread.start()