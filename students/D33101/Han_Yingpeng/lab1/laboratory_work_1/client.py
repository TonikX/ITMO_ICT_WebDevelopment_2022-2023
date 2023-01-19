import socket
 
so = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 4800)
 
while True:
    msg = input("Message: ")
    if not msg: continue
    so.sendto(msg.encode(), server_addr)
    res, server_addr = so.recvfrom(1024)
    print(f'Server: {res.decode()}\n')
    if msg == "q": break
print(f"Disconnected...")
so.close()