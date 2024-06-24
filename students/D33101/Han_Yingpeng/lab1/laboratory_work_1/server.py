import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4800))
print("Server up")
 
while True:
    data, client_addr = s.recvfrom(1024)
    print(f"Client message: {data.decode()}\n")
    if data == b"Hello, server": s.sendto(b"Hello, client", client_addr)
    elif data == b"q": s.sendto(b"Chao!", client_addr)
    else: s.sendto(b"Bla-bla-bla", client_addr)

s.close()