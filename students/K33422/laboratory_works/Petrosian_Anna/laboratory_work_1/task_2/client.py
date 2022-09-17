import socket
 
port = 3968
host = socket.gethostbyname("localhost")
#host="127.0.0.1"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #_stream for tcp dgram udp
 
sock.connect((host, port))
 
#data = sock.recv(1024)

a=input('Type the first variable x^2  ')
b=input('Type the second linear vatiable x  ')
c=input('Type the third variable  ')
#sock.send(int.from_bytes([a,b,c],byteorder='big',signed=True))
equation=a +" "+ b +" "+ c
sock.send(equation.encode('utf-8'))
#sock.send(a,b,c)
data = (sock.recv(1024)).decode('utf-8')
print(data)
#print (message)
#message = bytes(mess, 'utf-8')
#print(data.decode())
#print (message)
sock.close()
