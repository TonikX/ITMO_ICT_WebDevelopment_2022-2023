import socket
HOST = '127.0.0.1'
PORT = 14900
s = socket.socket()
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    cliensocket.send(b'Hello cleint')
    msg = cliensocket.recv(1024)
    if not msg:
        break
    print(msg.decode("utf-8"))
    cliensocket.close()
