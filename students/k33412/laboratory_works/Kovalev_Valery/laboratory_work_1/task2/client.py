import socket


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 9091))
    print("I solve Pythagorean theorem")
    a = ""
    while not a.isdigit():
        a = input("Enter a side A: ")
    b = ""
    while not b.isdigit():
        b = input("Enter a side B: ")

    while True:
        data = sock.recv(1024).decode()
        if data == "Side A":
            sock.send(a.encode())
        if data == "Side B":
            sock.send(b.encode())
        if data.startswith("Result"):
            print(data)
            break


if __name__ == "__main__":
    client()
