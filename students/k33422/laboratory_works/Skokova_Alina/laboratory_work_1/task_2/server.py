import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9998))
server.listen(1)
client, address = server.accept()

print(f"Connected to {address}")

client.send("Let's find the area of your trapezoid!".encode('utf-8'))
data = client.recv(1024).decode('utf-8')
values = data.split()
area = (float(values[0]) + float(values[1])) * float(values[2]) * 0.5
if area > 0:
    client.send(f"The area of your trapezoid = {area}".encode('utf-8'))
else:
    client.send("Error! Check your values".encode('utf-8'))

client.close()