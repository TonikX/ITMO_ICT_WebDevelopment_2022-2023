import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
data_from_client = conn.recv(16384)
udata = data_from_client.decode("utf-8")
print("Data: " + udata)
message_to_client = b"Hello, client! \n"
conn.send(message_to_client)
conn.close()