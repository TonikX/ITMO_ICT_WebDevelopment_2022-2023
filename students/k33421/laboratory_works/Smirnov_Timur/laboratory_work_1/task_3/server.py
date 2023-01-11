import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 9090))
    sock.listen(1)

    while True:
        try:
            conn, addr = sock.accept()

            response_type = "HTTP/1.0 200 OK\n"
            headers = "Content-Type: text/html\n\n"

            with open('index.html', 'r') as f:
                body = f.read()

            res = response_type + headers + body

            conn.send(res.encode('utf-8'))
            conn.close()
        except KeyboardInterrupt:
            sock.close()
            break


if __name__ == "__main__":
    main()
