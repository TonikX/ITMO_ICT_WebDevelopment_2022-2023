import socket, threading, time

shutdown = False

def recive():
    while not shutdown:
        try:
            data = s.recv(1024).decode('utf-8')
            print(data)
        except socket.error:
            time.sleep(0.5)
            continue


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090
s.connect((host,port))
s.setblocking(0)

alias = input("Name: ")
print('If you want to leave the chat write: bye')
rt = threading.Thread(target = recive)
rt.start()


while True:
    try:
        message = input()
        s.sendall((f'{alias} :: {message}').encode('utf-8'))
        if message == 'bye':
            print('You left the chat')
            shutdown = True
            break
    except:
        s.sendall('Error'.encode('utf-8'))
        print('Error. Disconected')
        shutdown = True
        break
s.close()