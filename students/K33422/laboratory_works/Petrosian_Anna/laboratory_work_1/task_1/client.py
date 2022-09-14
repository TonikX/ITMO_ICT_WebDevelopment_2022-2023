import socket
 
port = 631
host = socket.gethostbyname("localhost")
mess="Hello, server"
message = bytes(mess, 'utf-8')
#host="127.0.0.1"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
sock.connect((host, port))
sock.send(message)
 
data = sock.recv(1024)
print(str(message)[2:-1])
#print (message)
sock.close()
