import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 9090))
sock.send(b"Hello, server \n")
text=sock.recv(9111989)
dec_data=text.decode("utf-8")
print(dec_data)