import socket
import threading

nickname = input("Name: ")
client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_conn.connect(('127.0.0.1', 4800))

def get():
    while True:
        try:
            msg = client_conn.recv(1024).decode()
            if msg == 'reg':
                client_conn.send(nickname.encode())
            else:
                print(msg)
        except:
            break
        
def send():
    while True:
        message = input('')
        if message == 'stop':
            client_conn.close()
            break
        client_conn.send(message.encode())

# Starting Threads For Listening And Writing
get_thread = threading.Thread(target = get)
get_thread.start()

send_thread = threading.Thread(target = send)
send_thread.start()