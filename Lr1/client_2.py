import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 8888))
data = input("Введите длину основания 1, основания 2 и высоту: ")
sock.send(data.encode("utf-8"))
result = sock.recv(1024)
print(result.decode("utf-8"))
