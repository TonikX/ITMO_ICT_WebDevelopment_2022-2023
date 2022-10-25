import math
import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(("127.0.0.1", 8081))
conn.listen(10)
conn, addr = conn.accept()
message_to_client = b"Hello, client! \nWrite three paramets a, b, c with space:"
conn.send(message_to_client)
data_from_client = conn.recv(16384)
parametrs = data_from_client.decode("utf-8")
a = float(parametrs[0])
b = float(parametrs[2])
c = float(parametrs[4])
discr = b**2 - 4 * a * c
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    message_to_client = "x1 = %.2f \nx2 = %.2f" % (x1, x2)
elif discr == 0:
    x = -b / (2 * a)
    message_to_client = "x = %.2f" % x
else:
    message_to_client = "No roots"

conn.send(message_to_client.encode("utf-8"))

conn.close()
