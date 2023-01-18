import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((socket.gethostname(), 1234))
while True:
    data = sock.recv(1024)
    print(f"server: {data.decode()}")
    msg = input("Client: ")
    sock.send(str.encode(msg))