import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    try:
        clientsocket, addr = s.accept()
        print(f"Connection from {addr} has been established!")
        data = clientsocket.recv(1024)
        updata = data.decode('utf-8')
        print(updata)
        clientsocket.send(bytes("Hello client!", "utf-8"))
    except KeyboardInterrupt:
        s.close()
        break
