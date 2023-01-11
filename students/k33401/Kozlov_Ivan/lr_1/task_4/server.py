import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
conn.bind(("127.0.0.1", 8081))

clients = []
def send_message():
    while True:
        data, addr = conn.recvfrom(1024)
        if addr not in clients:
            clients.append(addr)
        for i in clients:
            if i == addr:
                continue
            conn.sendto(data, i)

send_message()

