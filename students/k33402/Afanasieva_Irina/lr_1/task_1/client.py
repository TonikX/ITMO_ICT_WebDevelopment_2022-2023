import socket

my_socket = socket.socket(socket.SOCK_DGRAM)
my_socket.connect(("127.0.0.10", 12400))
msg = "Hello, server!"
my_socket.send(msg.encode("utf-8"))
data = my_socket.recv(16384)
print(data.decode("utf-8"))
my_socket.close()
