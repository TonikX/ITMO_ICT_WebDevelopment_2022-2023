import socket, sys

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7272
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 1024
FORMAT = 'utf-8'
MISTAKE = "[INVALID INPUT] three coefficients needed, separated by space. Example: 1 2 3"
