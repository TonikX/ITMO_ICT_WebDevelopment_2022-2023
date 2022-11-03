import socket

s_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s_client.sendto(str.encode('Hello, server'), ('localhost', 9090))
rcvd = s_client.recvfrom(1024)

print("Message from Server: {}".format(rcvd[0].decode("utf-8")))