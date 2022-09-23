import socket

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7070
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 1024
FORMAT = 'utf-8'
CONNECT_MESSAGE = "Hello, server!".encode(FORMAT)

UDPClient = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClient.sendto(CONNECT_MESSAGE, ADDR)

msg, addr = UDPClient.recvfrom(BUFFER_SIZE)
print(f"[{addr}]: {msg.decode(FORMAT)}")
