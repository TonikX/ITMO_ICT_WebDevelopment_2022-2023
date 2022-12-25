import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9523))
sock.listen(10)
conn, addr = sock.accept()

print('connected with:', addr)

while True:
    data = conn.recv(1024)
    print(data.decode("utf-8"))
    if not data:
        break
    conn.send(b'Hello, client.\n')

conn.close()