import socket, sys


def main():
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.bind(("localhost", 9093))
    sock.listen(1)

    while True:
        conn, addr = sock.accept()
        conn.recv(16384)
        response_type = "HTTP/1.0 200 OK\n"
        headers = "Content-Type: text/html\n\n"
        file = open("index.html", "r")
        body = file.read()
        resp = response_type + headers + body
        conn.send(resp.encode("utf-8"))
        file.close()
        conn.close()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        sys.exit(0)
