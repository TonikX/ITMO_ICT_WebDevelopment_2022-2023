import socket
import threading
 
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
print('Leave from server - /LEAVE')
 
name = input("Enter your name: ")

client.connect(('127.0.0.1', 1337))
 
 
def outdatas():
    while True:
        outdata = input('')
        if outdata=='/LEAVE':
            break
        client.send(f'{name}: {outdata}'.encode('utf-8'))
        print(f'{name}: {outdata}')
 
 
def indatas():
    while True:
        indata = client.recv(1024)
        print(indata.decode('utf-8'))

t1 = threading.Thread(target=indatas, name='input')

t2 = threading.Thread(target=outdatas, name='out')

t1.start()
t2.start()

t2.join()
 
client.close()