from socket import *
import sys
import pickle
import threading


host = 'localhost'
port = 777
addr = (host, port)


def server_listener():
    while True:
        data = tcp_socket.recv(1024)
        data = data.decode().split('&')
        print(f"MESSAGE FROM USER {data[1]}:", data[0])


def cmd_listener():
    while True:
        my_message = input()
        tcp_socket.send(my_message.encode())



if __name__ == "__main__":
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.connect(addr)

    x = threading.Thread(target=server_listener, args=())
    y = threading.Thread(target=cmd_listener, args=())
    x.start()
    y.start()
