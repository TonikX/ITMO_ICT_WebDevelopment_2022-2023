import socket
import threading

host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
is_connected=False

def start_client():
    is_connected = True
    connection.connect(serv_addr)
    connection.send(input("Enter your name: ").encode("utf-8"))
    thread = threading.Thread(target=get_message)
    thread.start()
    while is_connected:
        message = input("")
        print("\033[A",end="")
        for i in range(0,len(message)):
            print(" ", end = "")
        print("\r",end="")
        connection.send(message.encode("utf-8"))
        if message == 'bye':
            get_message()
            is_connected=False
    connection.close()

def get_message():
    while is_connected:
        message = connection.recv(16384)
        message_dec = message.decode('utf-8')
        print(message_dec)

if __name__ == "__main__":
    start_client()