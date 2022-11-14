import socket

def serverImplementtaion():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.bind(('127.0.0.1', 9796))
    socketVar.listen(1)
    connection, address = socketVar.accept()

    print(f"Server conected to: {address}")

    while True:
        data = connection.recv(1024)
        if not data:
            break
        print(f"{data.decode('utf-8')} from {address[0]}:{address[1]}")
        connection.send(str.encode(f"Hello, {address[0]}:{address[1]}"))

    connection.close()


if __name__ == "__main__":
    serverImplementtaion()
