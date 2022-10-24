import socket

if __name__ == "__main__":
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(('localhost', 9090))
    abc = input().encode()
    sock.send(abc)

    data = sock.recv(1024)
    print(data.decode())
    sock.close()

