import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello server')

msg = s.recv(1024)
print(msg.decode("utf-8"))
