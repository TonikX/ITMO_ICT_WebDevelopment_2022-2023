import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8081))
print("Connect to server")
message_to_server = b"Hello, Server!"
conn.send(message_to_server)
data_from_server = conn.recv(16384)
print(data_from_server.decode("utf-8"))
conn.close()