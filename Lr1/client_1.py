import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))
sock.send(bytes("Hello, server! \n", "utf-8"))
msg = sock.recv(1024)
print(msg.decode("utf-8"))
