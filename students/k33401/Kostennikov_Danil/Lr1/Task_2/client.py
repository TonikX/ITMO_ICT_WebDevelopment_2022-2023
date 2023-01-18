import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

m = ''
while not m.isdigit():
    m = input("Enter m of trapezoid: ")

h = ''
while not h.isdigit():
    h = input("Enter h of trapezoid: ")

#s.send(b'Hello server')
s.send(m.encode())
s.send(h.encode())
res = s.recv(1024)
print(res.decode("utf-8"))
