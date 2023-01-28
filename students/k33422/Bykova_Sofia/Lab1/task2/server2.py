import socket
import sys

host = 'localhost'
port = 9090
addr = (host, port)

sock_serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_serv.bind(addr)
sock_serv.listen(5)

while True:
    clientsock, address = sock_serv.accept()
    data = clientsock.recv(4096)
    values = data.decode("utf-8")
    values = values.split(" ")
    h = float(values[0])
    s = float(values[1])
    # print(h, s, sep = ' ') для поиска ошибок
    square = h * s
    if square <= 0:
        clientsock.send((str('Ошибка. Значения не могут быть такими! Проверьте введённые данные.')).encode('utf-8'))
        sys.exit()

    clientsock.send(bytes(str(square), "utf-8"))

