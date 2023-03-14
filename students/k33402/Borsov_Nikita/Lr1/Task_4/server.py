from socket import *
import pickle
import logging
import threading
import time
import random

print('Server was started!')
all_messages = []


def thread_function(user_conn, user_addr):
    global all_messages
    print(f'client {user_addr} succesfully connected to our socket and send data')
    messages_copy = all_messages.copy()
    while True:
        time.sleep(0.1)
        # print('mc', messages_copy, '\n', 'am', all_messages)
        if messages_copy == all_messages:
            pass
        else:
            # print('HERE', (len(all_messages)-len(messages_copy))*(-1)-1)
            # print('mc:', messages_copy, 'am:', all_messages)
            # for i in range(-1, len(all_messages)-len(messages_copy)*(-1)-1, -1):
            #     print('i', i)

            user_conn.send((all_messages[-1][0]+"&").encode()+str(all_messages[-1][1]).encode())

            # print("sended", all_messages[-1])
            messages_copy = all_messages.copy()


def listener_function(user_conn, user_addr):
    global all_messages
    while True:
        data = user_conn.recv(1024)
        if data == b'':
            user_conn.close()
            break
        print(f'Message from client {user_addr[1]}', data)
        all_messages.append((''.join(data.decode()), user_addr[1]))
        time.sleep(3)


if __name__ == "__main__":
    host = 'localhost'
    port = 777
    addr = (host, port)

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen()

    while True:
        conn, addr = tcp_socket.accept()
        x = threading.Thread(target=thread_function, args=(conn, addr))
        y = threading.Thread(target=listener_function, args=(conn, addr))
        x.start()
        y.start()
        print("All thread are launched")
