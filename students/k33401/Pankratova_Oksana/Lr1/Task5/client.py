import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 3030))

msg1 = 'POST /grades?discipline=CV&name=Vasia&grade=4 HTTP/1.1\r\nHost: example.local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg1.encode('iso-8859-1'))
msg4 = s.recv(1024)
print(msg4.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 3030))

msg2 = 'GET /grades?discipline=CV HTTP/1.1\r\nHost: example.local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg2.encode('iso-8859-1'))
msg = s.recv(1024)
print(msg.decode())
s.close()
