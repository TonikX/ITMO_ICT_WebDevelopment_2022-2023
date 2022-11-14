import socket


def main():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.bind(('localhost', 8080))
    socketVar.listen(1)

    while True:
        conn, addr = socketVar.accept()
        # работа с файлом
        htmlPage = open('index.html')
        htmlContent = htmlPage.read()
        htmlPage.close()

        htmlResponse = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n' + htmlContent

        conn.sendall(htmlResponse.encode('utf-8'))
        conn.close()


if __name__ == '__main__':
    main()