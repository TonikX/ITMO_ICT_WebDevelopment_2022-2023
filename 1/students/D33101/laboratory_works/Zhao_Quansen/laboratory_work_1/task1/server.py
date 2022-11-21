import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 4245))
 
while True:
    data, addr = s.recvfrom(1024)
    print(f"Получено от {addr}\nЗапрос: {data.decode()}\n")
    if data == b"Hello, server":
        s.sendto(b"Hello, client", addr)
    else:
        s.sendto("Я не понимаю...".encode(), addr)

s.close()
print("Сервер закончил работу!")