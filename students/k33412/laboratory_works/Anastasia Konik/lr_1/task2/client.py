#Теорема Пифагора
import socket

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('localhost', 8081))
client_sock.sendall('Pyfagorean theorem'.encode("utf-8"))

data = client_sock.recv(1024)
print(data.decode("utf-8"))

sides = input()
client_sock.sendall(sides.encode("utf-8"))

data = client_sock.recv(1024)

client_sock.close()

print(data.decode("utf-8"))
