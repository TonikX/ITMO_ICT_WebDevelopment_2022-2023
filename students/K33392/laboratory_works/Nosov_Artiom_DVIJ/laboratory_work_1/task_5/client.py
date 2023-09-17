import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8080))

msg = 'POST /grades?discipline=theory_of_neural_network&name=Artiom&grade=5 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8080))

msg = 'POST /grades?discipline=theory_of_neural_network&name=Anna&grade=4 HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 8080))

msg = 'GET /grades?discipline=theory_of_neural_network HTTP/1.1\r\nHost: local\r\nAccept: text/html\r\nUser-Agent: Mozilla/5.0\r\n\r\n'
s.send(msg.encode('iso-8859-1'))
msg_recv = s.recv(1000)
print(msg_recv.decode())
s.close()
