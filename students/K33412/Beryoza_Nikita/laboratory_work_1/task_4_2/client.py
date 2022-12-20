import socket
import threading

HOST = '127.0.0.1'
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
username = input("Please Enter a User Name: ")


def read_message():
    while True:
        try:
            message = client.recv(1204).decode('ascii')
            if message == "UserName":
                client.send(username.encode('ascii'))
            else:
                print(message)
        except:
            print("Error!")
            client.close()
            break


def write_message():
    while True:
        message = f"{username}: {input(': ')}"
        client.send(message.encode("ascii"))


read_thread = threading.Thread(target=read_message)
read_thread.start()

write_thread = threading.Thread(target=write_message)
write_thread.start()