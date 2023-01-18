import socket
import threading

sock = socket.socket()
sock.connect(('localhost', 9090))

username = input('Name: ')

def accept_from_server():
    while True:
        msg = sock.recv(1024)
        print(msg.decode())

thread = threading.Thread(target=accept_from_server)
thread.start()


while True:
    try:
        message = input()
        sock.sendall(('[' + username + '] :: ' + message).encode())
    except:
        sock.sendall('Error'.encode())
        print('Error. Disconnected')
        break
sock.close()