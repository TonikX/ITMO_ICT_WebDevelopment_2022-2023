import socket
import threading

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 9090))

nick = input("Your nick: ")


def get_message():
    while True:
        try:
            message = client_sock.recv(1024)
            if len(message) == 0:
                client_sock.close()
                break

            if message.decode("utf-8") == 'Nick:':
                client_sock.sendall(nick.encode("utf-8"))
            else:
                print(message.decode("utf-8"))
        except:
            client_sock.close()
            break


def send_message():
    while True:
        try:
            text = input("")
            message = '{}:{}'.format(nick, text)
            client_sock.sendall(message.encode("utf-8"))
            if text == "bye":
                break
        except:
            client_sock.close()
            break


get_thread, send_thread = threading.Thread(target=get_message), threading.Thread(target=send_message)
get_thread.start()
send_thread.start()
