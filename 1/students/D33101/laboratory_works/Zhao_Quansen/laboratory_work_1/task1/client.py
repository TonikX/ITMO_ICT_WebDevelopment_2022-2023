import socket
 
socket_ = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', 4245)
 
message = input("Ваше сообщение: ")
socket_.sendto(message.encode(), server_addr)
response, server_addr = socket_.recvfrom(1024)
print(f'Ответ от сервера: {response.decode()}\n')
socket_.close()