import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.connect(("127.0.0.1", 8000))
data = input("Введите a и b через пробел: ")
conn.send(data.encode("utf-8"))
result = conn.recv(16384).decode("utf-8")
print("c = ", result)
conn.close()