import socket
 
sock = socket.socket()
sock.connect(('127.0.0.1', 1337))
 
 
data = sock.recv(1024)
print(data.decode("utf-8"))
 
sock.close()