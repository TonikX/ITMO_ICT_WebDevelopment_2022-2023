import socket

addressPort = ('127.0.0.1', 9090)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(addressPort)
data = sock.recv(1024)
print(data.decode("utf-8"))
sock.close()
