import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 9998))

print(client.recv(1024).decode('utf-8'))
client.send(input("Enter 3 values with a space separator (base1 base2 height): ").encode('utf-8'))
print(client.recv(1024).decode('utf-8'))

client.close()