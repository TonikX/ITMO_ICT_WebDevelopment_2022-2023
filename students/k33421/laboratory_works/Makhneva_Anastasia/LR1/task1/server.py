import socket

host = "localhost"
port = 2468
message = "Hello, client"
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
while True:
    received_message, address = server.recvfrom(4096)
    print("Client said: ", received_message.decode("utf-8"))
    server.sendto(message.encode("utf-8"), address)
    server.close()
    break
