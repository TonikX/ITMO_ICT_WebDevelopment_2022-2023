import socket

host = "localhost"
port = 14900

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

   #Version with trapezoid

for i in range(3):
    data = sock.recv(16384)
    text = data.decode()
    print(text)
    proportions = input()
    sock.send(proportions.encode())

data = sock.recv(16384)
trapezoid_area = data.decode()
print(trapezoid_area)
sock.close()