import socket
import math


def math_square(m_data):
    split_str = m_data.split()
    if split_str[0] == "a":
        return int(split_str[1]) * int(split_str[2])
    elif split_str[0] == "b":
        return int(split_str[1]) * int(split_str[2]) * math.sin(math.radians(int(split_str[3])))
    elif split_str[0] == "c":
        return (1 / 2) * int(split_str[1]) * int(split_str[2]) * math.sin(math.radians(int(split_str[3])))
    else:
        return 0


sock = socket.socket()
sock.bind(("", 8080))
sock.listen(1)
conn, addr = sock.accept()
try:
    while 1:
        try:
            conn.settimeout(10)
            data = conn.recv(16384)
            if not data:
                break
            decoded_data = data.decode("utf-8")
            massage_out = str(math_square(decoded_data))
            conn.send(massage_out.encode("utf-8"))
        except socket.error:
            print("connection timed out")
            break
        finally:
            conn.close()
finally:
    sock.close()
