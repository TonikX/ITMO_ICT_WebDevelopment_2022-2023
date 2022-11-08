import socket

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7171
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 64
FORMAT = 'utf-8'
