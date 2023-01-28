import socket

host = 'localhost'
port = 9090
addr = (host, port)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(addr)

while True:
    msg = s.recvfrom(1024)
    message = msg[0].decode('utf-8')
    clientMsg = 'Message from client: {}'.format(message)

    print(clientMsg)
    s.sendto(str.encode('Hello, client!'))

