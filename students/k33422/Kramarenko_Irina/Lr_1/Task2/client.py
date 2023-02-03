import socket

def main():
    s_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_ip = input("Введите IP-адрес сервера, к которому вы хотите подлючиться:")
    # server_port = int(input("Введите порт сервера:"))
    # s_client.connect((server_ip, server_port))
    s_client.connect(('localhost', 9090))
    client_msg = input("Введите длину стороны и высоты параллелограмма:")
    # client_height = input("Введите высоту:")
    s_client.send(client_msg.encode("utf-8")) #, ('localhost', 9090))
    rcvd = s_client.recv(1024)
    print("Площадь параллелограмма:" + rcvd.decode("utf-8"))
    s_client.close()

if __name__ == "__main__":
    main()