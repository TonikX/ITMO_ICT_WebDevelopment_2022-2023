from config import *


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"You are connected to {HOST}:{PORT}, "
          f"which calculates the roots of the quadratic equation:"
          f" a*x^2 + b*x + c = 0")
    while True:
        try:
            inp = input("Enter the a, b, c: ")
            values = [float(i) for i in inp.split(' ')]
            if len(values) != 3:
                raise ValueError
            client.sendall(inp.encode(FORMAT))
            print(f"Answer: {client.recv(1024).decode(FORMAT)}")
            break
        except ValueError:
            print(MISTAKE)


if __name__ == "__main__":
    main()
