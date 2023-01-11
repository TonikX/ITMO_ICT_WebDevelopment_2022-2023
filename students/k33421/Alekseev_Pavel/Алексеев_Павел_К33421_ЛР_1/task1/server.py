import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8888))
sock.listen(100)
sock, addr = sock.accept()

client_to_server = sock.recv(2048)
print("Data from client: " + client_to_server.decode("utf-8"))

server_to_client = b"Hello, client!"
sock.send(server_to_client)

sock.close()