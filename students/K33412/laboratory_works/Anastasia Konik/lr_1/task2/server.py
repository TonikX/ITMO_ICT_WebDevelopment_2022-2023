# Теорема Пифагора
import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('localhost', 8081))
server_sock.listen(5)

while True:
    client_sock, client_addr = server_sock.accept()
    data = client_sock.recv(1024)
    if not data:
        break
    print(data.decode("utf-8"))
    client_sock.sendall('Enter the sides (for ex. 5,9)'.encode("utf-8"))

    data = client_sock.recv(1024)
    sides = data.decode("utf-8")

    try:
        a, b = map(int, sides.split(','))
        c = (a ** 2 + b ** 2) ** 0.5
        ans = str(round(c, 3))
        client_sock.sendall(ans.encode("utf-8"))
    except Exception:
        client_sock.sendall('Error. Try again'.encode("utf-8"))

    client_sock.close()
