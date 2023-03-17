import socket
import threading

host = "127.0.0.1"
port = 14900
serv_addr = (host, port)
connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
exit_event = threading.Event()

def start_client():
    is_conn = True
    connection.connect(serv_addr)
    connection.send(input("Enter your name: ").encode("utf-8"))
    thread = threading.Thread(target=get_message)
    thread.start()
    while is_conn:
        message = input("")
        print("\033[A",end="")
        for i in range(0,len(message)):
            print(" ", end = "")
        print("\r",end="")
        if message == 'bye':
            exit_event.set()
            is_conn = False
        connection.send(message.encode("utf-8"))
    connection.close()

def get_message():
    while True:
        if exit_event.is_set():
            break
        try:
            message = connection.recv(16384)
            message_dec = message.decode('utf-8')
            print(message_dec)
        except:
            break
   
if __name__ == "__main__":
    start_client()