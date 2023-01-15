import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

full_msg = ''
while True:
    msg = s.recv(1024)
    if len(msg) <=0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)
