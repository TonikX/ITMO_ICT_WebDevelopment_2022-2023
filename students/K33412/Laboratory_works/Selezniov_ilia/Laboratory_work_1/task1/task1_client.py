import socket


HOST, PORT = "localhost", 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall(bytes("Hello, server" + "\n", "utf-8"))

    received = str(sock.recv(1024), "utf-8")
    print(f"Received data: {received}")
