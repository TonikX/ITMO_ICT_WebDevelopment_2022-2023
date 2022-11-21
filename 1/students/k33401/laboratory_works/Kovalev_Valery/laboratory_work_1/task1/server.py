import socket


def server():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9090))
    sock.listen(1)
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"{data.decode('utf-8')} from {addr[0]}:{addr[1]}")
        conn.send(str.encode(f"Hello, {addr[0]}:{addr[1]}"))

    conn.close()


if __name__ == "__main__":
    server()
