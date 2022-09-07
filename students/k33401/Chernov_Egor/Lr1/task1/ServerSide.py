import socket

sock = socket.socket()

# if "127.0.0.1" - connect only my cp host, if "0.0.0.0"- connect all hosts
# 8080 - port
sock.bind(("", 8080))
# set listening and queue size
sock.listen(1)
# accept() return client socket and client address
# Адрес — массив, состоящий из IP-адреса и порта
conn, addr = sock.accept()
# get data
data = conn.recv(16384)
decodeData = data.decode("utf-8")
print("Server: " + decodeData)
# two ways for send data, in both ways data should be encoded
massage = "Hello, client"
# conn.send(b"Hello, client\n")
conn.send(massage.encode("utf-8"))
# close connection
conn.close()
