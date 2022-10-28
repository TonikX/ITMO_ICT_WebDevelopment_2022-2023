import socket
HOST = '127.0.0.1'
PORT = 14900

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()

while True:
    cliensocket, address = s.accept()
    print(f"Connection from {address} has been esteblished")
    m = float(cliensocket.recv(1024).decode())
    if not m:
        break
    #print(m)
    h = float(cliensocket.recv(1024).decode())
    if not h:
        break    
    #print(h)
    res = m*h
    res = str(res)
    cliensocket.send(res.encode())

cliensocket.close()
