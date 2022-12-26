import socket

sock = socket.socket()
sock.bind(('localhost', 7777))
sock.listen(1)
clientSocket, addr = sock.accept()

print('connected:', addr)

while True:
    data = clientSocket.recv(1024)
    data = data.decode('utf-8')
    print(data)
    if not data:
        break
    clientSocket.send('Hello, client'.encode('utf-8'))

sock.close()