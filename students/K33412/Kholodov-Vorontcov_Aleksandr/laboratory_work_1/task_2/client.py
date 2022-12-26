import socket


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 7778))
    print("Quadratic equation solver")
    a = ""
    while not a.isdigit():
        a = input("Insert 'a': ")
    b = ""
    while not b.isdigit():
        b = input("Insert 'b': ")
    c = ""
    while not c.isdigit():
        c = input("Insert 'c': ")

    while True:
        data = sock.recv(1024).decode('utf-8')
        if data == 'a':
            sock.send(a.encode('utf-8'))
        if data == 'b':
            sock.send(b.encode('utf-8'))
        if data == 'c':
            sock.send(c.encode('utf-8'))
        if data.startswith("Result"):
            print(data)
            break


if __name__ == "__main__":
    client()
