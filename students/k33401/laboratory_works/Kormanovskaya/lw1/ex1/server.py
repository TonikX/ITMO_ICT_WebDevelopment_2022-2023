import socket

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7070
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 1024
FORMAT = 'utf-8'
CONNECT_MESSAGE = "Hello, client!".encode(FORMAT)

UDPServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServer.bind(ADDR)


def start():
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    while True:
        msg, addr = UDPServer.recvfrom(BUFFER_SIZE)
        print(f"[{addr}]: {msg.decode(FORMAT)}")
        UDPServer.sendto(CONNECT_MESSAGE, addr)


print("[STARTING] server is starting...")
start()