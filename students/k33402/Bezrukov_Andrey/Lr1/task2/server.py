import socket
import math

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(('localhost', 10001))
conn.listen(10)
conn, addr = conn.accept()

data_from_client = conn.recv(5096)
cat = data_from_client.decode("utf-8")

r = cat.split()
a = float(r[0])
b = float(r[1])
c = round(math.sqrt(a**2 + b**2), 3)

conn.send(str(c).encode("utf-8"))

conn.close()