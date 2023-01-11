import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('', 8888))


client_to_server = b"Hello, server!"
sock.send(client_to_server)

server_to_client = sock.recv(2048)
print("Data from server: " + server_to_client.decode("utf-8"))

sock.close()