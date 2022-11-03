import socket

host = 'localhost'
port = 9090
addr = (host, port)

s_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_server.bind(addr)

while True:
    rcvd = s_server.recvfrom(1024)
    print("Message from client: {}".format(rcvd[0].decode("utf-8")))
    s_server.sendto(str.encode("Hello, client"), rcvd[1])