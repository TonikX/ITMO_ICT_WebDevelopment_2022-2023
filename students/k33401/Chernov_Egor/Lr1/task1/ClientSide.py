import socket

sock = socket.socket()

# connect to port which is listening server
sock.connect(("127.0.0.1", 8080))
massage = "Hello, server"
sock.send(massage.encode("utf-8"))
data = sock.recv(16384)
decodeData = data.decode("utf-8")
print("Client: " + decodeData)
