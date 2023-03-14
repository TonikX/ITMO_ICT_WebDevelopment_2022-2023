import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 4462))


data = sock.recv(24000)
print(data.decode())

v = str(input())
sock.send(v.encode())
data = sock.recv(24000)
print(data.decode())

if(data.decode() != "Таких вычислений нет'\n'"):
    resps = input()
    sock.send(resps.encode())
    data = sock.recv(24000)
    print(data.decode())


sock.close()

