import socket
from threading import Thread

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7474
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 64
FORMAT = 'utf-8'
ASKING = "Enter your username: "
