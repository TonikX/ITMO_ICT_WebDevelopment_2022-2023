import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9090))
server.listen(1)
client, address = server.accept()

print(f"Connected to {address}")

with open('index.html', 'r') as f:
   page = f.read() 

client.send(f"HTTP/1.0 200 OK\nContent-Type: text/html\n\n{page}".encode('utf-8'))

client.close()