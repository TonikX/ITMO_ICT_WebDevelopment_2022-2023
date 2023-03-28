import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
a = input("length of the upper base of your trapezoid: ")
print()
b = input("length of the lower base of your trapezoid: ")
print()
h = input("length of the height of your trapezoid: ")
print()
a = a.encode("utf-8")
b = b.encode("utf-8")
h = h.encode("utf-8")
while not a.isdigit():
    print("this value must be a number")
    print()
    a = input("length of the upper base of your trapezoid: ")
    print()
    a = a.encode("utf-8")
while not b.isdigit():
    print("this value must be a number")
    print()
    b = input("length of the lower base of your trapezoid: ")
    print()
    b = b.encode("utf-8")
while not h.isdigit():
    print("this value must be a number")
    print()
    h = input("length of the height of your trapezoid: ")
    print()
    h = h.encode("utf-8")

while True:
    data = client.recv(4096)
    data = data.decode("utf-8")
    if data == "upper base of the trapezoid":
        client.sendto(a, (host, port))
    if data == "lower base of the trapezoid":
        client.sendto(b, (host, port))
    if data == "height of the trapezoid":
        client.sendto(h, (host, port))
    if data.startswith("The area"):
        print(f"server calculated the area of the trapezoid with the parameters:\n"
              f"    1) length of the upper base of your trapezoid: {float(a)}\n"
              f"    2) length of the lower base of your trapezoid: {float(b)}\n"
              f"    3) length of the height of your trapezoid: {float(h)}\n")
        print(data)
        break

client.close()
