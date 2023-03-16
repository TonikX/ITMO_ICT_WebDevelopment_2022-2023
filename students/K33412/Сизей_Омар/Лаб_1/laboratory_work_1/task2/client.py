import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 14900))

for i in range(3):
    data = sock.recv(1024)
    text = data.decode()
    print(text)
    proportions = input()
    sock.send(proportions.encode())

data = sock.recv(1024)
parallelogram_area = data.decode()
print(parallelogram_area)
sock.close()
