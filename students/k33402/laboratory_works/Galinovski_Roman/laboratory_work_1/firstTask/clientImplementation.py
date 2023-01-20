import socket

def clientImplementation():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.connect(('127.0.0.1', 9796))
    socketVar.send(b'Hello, server!')

    data = socketVar.recv(1024)
    socketVar.close()

    print(data.decode("utf-8"))


if __name__ == "__main__":
    clientImplementation()