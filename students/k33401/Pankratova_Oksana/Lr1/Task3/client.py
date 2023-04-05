import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1212))
msg = ''
while True:
    line = s.recv(1024)
    if not line:
        break
    msg += line.decode()

print(msg)

s.close()
