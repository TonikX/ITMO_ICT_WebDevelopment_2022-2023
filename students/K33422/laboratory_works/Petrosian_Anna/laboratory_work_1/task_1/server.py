import socket
 
port = 3968
host = socket.gethostbyname("localhost")

#host="127.0.0.1"

mess="Hello, client"
message = bytes(mess, 'utf-8')
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #use TCP

"""#const int optval=1
setsockopt(sock, SOL_SOCKET, SO_REUSEADDR, &optval, sizeof(optval))
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # CREATING A SOCKET from documentation, интернет-протокол, установление двустороннего обмена инфой
sock.close() #aready used, so close, please
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #so reestablish, please
sock.connect((host, port))"""
#int sock = 1
"""if (setsockopt (listener, SOL_SOCKET, SO_REUSEADDR, & sock, sizeof (opt)) == -1):
	perror("setsockopt")
else:
	print('aaaaaaaaa')"""

sock.bind((host, port)) #связь сокета с хостом и портом
sock.listen(10) #n listenings 
cl_sock, addr = sock.accept() #приём и посылка данных
data = cl_sock.recv(1024) #порция данных
print(data.decode())
cl_sock.send(message)

sock.close() #закрыли соединени
