import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((socket.gethostname(), 9090))

while True:
    msg, address = s.recvfrom(1024)
    print(msg.decode())
    s.sendto(bytes('Hello, client', 'utf-8'), address)

s.close()
