from socket import *

host = 'localhost'
port = 777
addr = (host, port)

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(addr)

print('Server was started!')

while True:
    data, addr = udp_socket.recvfrom(1024)
    print(f'client {addr} succesfully connected to our socket with mesage \n```\n{data.decode("utf-8")}\n```')
    udp_socket.sendto(b'Hello client', addr)

# udp_socket.close() As part of my expirience if you use Ctrl+C for exit, socket connection will be automatically
# destroyed, I check with `sudo lsof -i:777`
