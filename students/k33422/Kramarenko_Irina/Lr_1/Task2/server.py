import socket

host = 'localhost'
port = 9090
addr = (host, port)

def main():
    s_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_server.bind(addr)
    s_server.listen(1)

    while True:
        print("Ожидание клиентской ссылки...")
        s_client, client_addr = s_server.accept()
        print("Клиентское соединение успешно")
        while True:
            rcvd = s_client.recv(1024)
            print(rcvd.decode("utf-8"))
            if rcvd:
                a, height = map(lambda x: int(x), rcvd.split())
                square = a * height
                s_client.send(str(square).encode("utf-8"))
            else:
                break
        s_client.close()
    s_server.close()

if __name__ == "__main__":
    main()
