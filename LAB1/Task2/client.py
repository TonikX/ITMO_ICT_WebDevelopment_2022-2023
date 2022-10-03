import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 9090))
s = input("Enter the base:")
h = input("Enter the height:")
sock.send(s.encode())
sock.send(h.encode())

msg = sock.recv(1024)
print(msg.decode("utf-8"))
sock.close()