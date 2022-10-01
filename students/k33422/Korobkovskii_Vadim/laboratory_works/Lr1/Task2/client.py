import socket

host = "localhost"
port = 2468
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
a = input("Enter the length of the upper base of the trapezoid: ")
print()
b = input("Enter the length of the lower base of the trapezoid: ")
print()
h = input("Enter the length of the height of the trapezoid: ")
print()
a = a.encode("utf-8")
b = b.encode("utf-8")
h = h.encode("utf-8")
while not a.isdigit():
    print("The length of the upper base of the trapezoid must be a number! Try again, please!")
    print()
    a = input("Enter the length of the upper base of the trapezoid: ")
    print()
    a = a.encode("utf-8")
while not b.isdigit():
    print("The length of the lower base of the trapezoid must be a number! Try again, please!")
    print()
    b = input("Enter the length of the lower base of the trapezoid: ")
    print()
    b = b.encode("utf-8")
while not h.isdigit():
    print("The length of the height of the trapezoid must be a number! Try again, please!")
    print()
    h = input("Enter the length of the height of the trapezoid: ")
    print()
    h = h.encode("utf-8")

while True:
    data = client.recv(4096)
    data = data.decode("utf-8")
    if data == "Upper base of the trapezoid":
        client.sendto(a, (host, port))
    if data == "Lower base of the trapezoid":
        client.sendto(b, (host, port))
    if data == "The height of the trapezoid":
        client.sendto(h, (host, port))
    if data.startswith("The area"):
        print(f"Server calculated the area of the trapezoid with next parameters:\n"
              f"    1) Length of the upper base of the trapezoid: {float(a)}\n"
              f"    2) Length of the lower base of the trapezoid: {float(b)}\n"
              f"    3) Length of the height of the trapezoid: {float(h)}\n")
        print(data)
        break

client.close()