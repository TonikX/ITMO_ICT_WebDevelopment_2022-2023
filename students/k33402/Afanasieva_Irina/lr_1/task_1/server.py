import socket

my_socket = socket.socket(socket.SOCK_DGRAM)
my_socket.bind(("127.0.0.10", 12400))
my_socket.listen(10)

sock, address = my_socket.accept()
data = sock.recv(16384)
data = data.decode("utf-8")
print(data)
msg = "Hello, client!"
sock.send(msg.encode("utf-8"))
my_socket.close()
