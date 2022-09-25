import socket

# address properties
HOST = socket.gethostbyname(socket.gethostname())
PORT = 7373
ADDR = (HOST, PORT)
# message properties
BUFFER_SIZE = 1024
FORMAT = 'utf-8'


def send_answer(conn, status="200 OK", typ="text/html; charset=utf-8", data=""):
    conn.send(b"HTTP/1.1 " + status.encode(FORMAT) + b"\r\n")
    conn.send(b"Server: simplehttp\r\n")
    conn.send(b"Connection: close\r\n")
    conn.send(b"Content-Type: " + typ.encode(FORMAT) + b"\r\n")
    conn.send(b"\r\n")
    conn.send(data.encode(FORMAT))


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[STARTED] Server is listening on {HOST}:{PORT}")
    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE)
        if not data:
            break
        print(f"[NEW CONNECTION]: {addr[0]}:{addr[1]}")
        send_answer(conn, data=open('index.html', 'r').read())
        conn.close()


if __name__ == "__main__":
    main()
