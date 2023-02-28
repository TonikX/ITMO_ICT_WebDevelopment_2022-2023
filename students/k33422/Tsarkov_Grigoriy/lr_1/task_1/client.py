import socket

addressPort = ('127.0.0.1', 9090)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(addressPort)
sock.sendto(b"hello, world! \n", addressPort)

data = sock.recvfrom(1024)
sock.close()

print(data[0].decode("utf-8"))
