import socket, sys


def calc_parallelogram_area(side, height):
    return side * height


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(("localhost", 9092))
    sock.listen(1)

    conn, addr = sock.accept()

    while True:
        data = conn.recv(1024)
        if not data:
            break
        s, h = [int(i) for i in data.decode().split("\n")]
        conn.send(str.encode(str(calc_parallelogram_area(s, h))))
    conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
