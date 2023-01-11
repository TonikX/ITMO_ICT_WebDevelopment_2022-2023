import socket
import math

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 8001))
sock.listen(10)
sock, addr = sock.accept()

data_from_client = sock.recv(5096)
cat = data_from_client.decode("utf-8")

r = cat.split()
a = float(r[0])
b = float(r[1])
gep = round(math.sqrt(a**2 + b**2), 3)
ms_to_cl = str(gep)

sock.send(ms_to_cl.encode("utf-8"))

sock.close()