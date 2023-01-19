from socket import *

tcp = socket(AF_INET,SOCK_STREAM)
tcp.connect(('127.0.0.1', 4800))

tcp.send('get adress'.encode())
webpage_http = tcp.recv(1024)
print(webpage_http.decode())

tcp.close()