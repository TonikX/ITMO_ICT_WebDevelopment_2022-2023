import socket

s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_client.connect(('localhost', 9090))
s_client.send('Hello, server'.encode("utf-8"))
rcvd = s_client.recv(1024)
print(rcvd.decode("utf-8"))
s_client.close()
# print("Message from Server:{}".format(rcvd[0]))