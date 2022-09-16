import socket
 
<<<<<<< HEAD
port = 3968
=======
port = 631
>>>>>>> 6892f16625ccaab2d2b29b3f91b357044e17f3df
host = socket.gethostbyname("localhost")
mess="Hello, server"
message = bytes(mess, 'utf-8')
#host="127.0.0.1"
<<<<<<< HEAD
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
=======
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
>>>>>>> 6892f16625ccaab2d2b29b3f91b357044e17f3df
 
sock.connect((host, port))
sock.send(message)
 
data = sock.recv(1024)
<<<<<<< HEAD
print(data.decode())

=======
print(str(message)[2:-1])
#print (message)
>>>>>>> 6892f16625ccaab2d2b29b3f91b357044e17f3df
sock.close()
