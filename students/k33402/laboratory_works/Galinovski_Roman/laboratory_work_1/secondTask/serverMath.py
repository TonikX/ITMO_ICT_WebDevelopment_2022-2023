import socket
import math

def pifagor(data):
    return int(data[1]) * int(data[2])

def parallelogramArea(data):
    return int(data[1]) * int(data[2]) * math.sin(math.radians(int(data[3])))

def trapezoidArea(data):
    return (1 / 2) * int(data[1]) * int(data[2]) * math.sin(math.radians(int(data[3])))

def mathAreas(_data):
    splitData = _data.split()

    if splitData == "a":
        return pifagor(splitData)
    elif splitData == "b":
        return parallelogramArea(splitData)
    elif splitData == "c":
        return trapezoidArea(splitData)
    else:
        return 0

def server():
    sock = socket.socket()
    sock.bind(('127.0.0.1', 9080))
    sock.listen(1)
    connection, address = sock.accept()

    try:
        while 1:
            try:
                connection.settimeout(10)
                data = connection.recv(16384)
                if not data:
                    break
                decData = data.decode("utf-8")
                massage_out = str(mathAreas(decData))
                connection.send(massage_out.encode("utf-8"))
            except socket.error:
                print("connection timed out")
                break
            finally:
                connection.close()
    finally:
        sock.close()

if __name__ == "__main__":
    server()