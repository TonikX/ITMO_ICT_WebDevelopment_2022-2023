import socket

host = "localhost"
port = 2468
message = "Hello, server"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
client.sendto(message.encode("utf-8"), (host, port))
received_message, address = client.recvfrom(4096)
print("Server said: ", received_message.decode("utf-8"))
client.close()
