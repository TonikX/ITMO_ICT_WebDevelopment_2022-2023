from socket import *
import webbrowser

LOCALHOST = "127.0.0.1"
PORT = 3000

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((LOCALHOST, PORT))
tcp_socket.send("989796".encode())


while True:
    res = tcp_socket.recv(4096)
    res = res.decode()
    if res == '':
        tcp_socket.close()
        break
    data = res.split('\n')
    print(data)
    if data[0].split()[1] == '200' and len(data) == 2:
        data = input("Что вы хотите?\n")
        tcp_socket.send(data.encode())
        continue
    elif data[0].split()[1] == '200' and len(data) > 2:
        f = open('file_test_2.html', 'wb')
        f.write(data[2].encode())
        f.close()
        url = 'file://C:/Users/Никита/PycharmProjects/ITMO_ICT_WebDevelopment_2022-2023/students/K33412/Beryoza_Nikita/laboratory_work_1/file_test_2.html'
        webbrowser.open(url, new=2)
        tcp_socket.close()
        break

