import socket
#import urllib
import codecs
port = 3968
host = socket.gethostbyname("localhost")

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #use TCP

"""page = urllib.urlopen("index.html").read()
page = urllib.request.urlopen("/path/").read() 
print(page) 
page_content = page.read()
print(page_content)

mess="Hello, client"
message = bytes(mess, 'utf-8')"""

f = codecs.open("index.html", 'r', 'utf-8')
pg=f.read()


sock.bind((host, port)) #связь сокета с хостом и портом
sock.listen(10) #n listenings 
cl_sock, addr = sock.accept() #приём и посылка данных
data = cl_sock.recv(1024) #порция данных
print(data.decode())
cl_sock.sendall(pg) #page_content

sock.close() #закрыли соединени