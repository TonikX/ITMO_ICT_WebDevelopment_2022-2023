import socket

port = 14900
host = "127.0.0.1"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CREATING A SOCKET from documentation
#интернет-протокол, установление двустороннего обмена инфой
sock.bind((host, port)) #связь сокета с хостом и портом
sock.listen(1) #режим прослушивания


cl_sock, addr = sock.accept() #приём и посылка данных
data = cl_sock.recv(1024) #порция данных
print(data)
cl_sock.send("Hello, client")

sock.close() #закрыли соединение