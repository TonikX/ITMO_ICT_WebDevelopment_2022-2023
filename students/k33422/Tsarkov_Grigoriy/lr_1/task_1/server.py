import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))
data = sock.recvfrom(1024)
print(data[0].decode("utf-8"))
sock.sendto(b"hello, client! \n", data[1])
sock.close()
