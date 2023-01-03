import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")
sock.bind(("127.0.0.1", 9091))
sock.listen(5)
print("waiting for conn")

while True:
    clientside, address = sock.accept()
    print(f"Connected: {address} has been established")
    clientside.send(str.encode(f"Hello, client!", "utf-8"))
    clientside.close()


