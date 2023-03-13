import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 5678))

server_socket.listen(5)

def calculate_area_of_trapezoid(base1, base2, height):
    return (base1 + base2) / 2 * height

while True:
    client_socket, address = server_socket.accept()
    client_socket.send('Enter parameters of trapezoid separated by space: base1 base2 height'.encode())
    data = client_socket.recv(1024).decode('ascii').split(' ')
    result = calculate_area_of_trapezoid(int(data[0]), int(data[1]), int(data[2]))
    client_socket.send(str(result).encode())
