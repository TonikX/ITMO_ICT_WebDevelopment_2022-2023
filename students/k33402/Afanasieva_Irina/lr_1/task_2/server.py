# Variant ф. - теорема пифагора
import socket
import math

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind(("127.0.0.1", 12400))

my_socket.listen(10)

sock, address = my_socket.accept()
sock.send("Input a:".encode())
a = int(sock.recv(16384).decode())  # Первый катет
sock.send("Input b:".encode())
b = int(sock.recv(16384).decode())  # Второй катет
c = a * a + b * b
result = math.sqrt(c)
sock.send(f"The result is:\n {result}".encode())
my_socket.close()
