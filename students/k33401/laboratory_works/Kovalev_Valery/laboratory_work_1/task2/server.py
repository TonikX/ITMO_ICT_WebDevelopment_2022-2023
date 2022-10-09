import socket


def pythagorean_theorem(a, b):
    return a * a + b * b


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 9091))
    sock.listen()
    conn, addr = sock.accept()

    print(f"Connected: {addr}")

    a = ""
    b = ""
    result = ""

    while not result:
        while not a:
            conn.send("Side A".encode())
            data = conn.recv(1024).decode()
            if data.isdigit():
                a = float(data)

        while not b:
            conn.send("Side B".encode())
            data = conn.recv(1024).decode()
            if data.isdigit():
                b = float(data)

        result = pythagorean_theorem(a, b)
        conn.send(str.encode(f"Result is {result}"))

    conn.close()


if __name__ == "__main__":
    server()
