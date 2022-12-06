import socket


HOST, PORT = "localhost", 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))
    sock.sendall((
        b"GET /index.html HTTP/1.1\r\n" +
        bytes(f"Host: {HOST}\r\nAccept: text/html\r\nConnection: close\r\n\r\n",
              "utf-8")))
    received = str(sock.recv(1024), "utf-8")
    print(received)
