import socket 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 555))
data = s.recv(1024) #получаем сообщение из сокета.
print(data.decode('utf-8'))
s.close()