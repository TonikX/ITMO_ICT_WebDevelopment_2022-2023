from socket import *
import sys
import pickle


host = 'localhost'
port = 777
addr = (host, port)

tcp_socket = socket(AF_INET, SOCK_STREAM)

while True:
    try:
        a = float(input("Please input the lower base of the trapezoid: "))
        b = float(input("Please input the upper base of the trapezoid: "))
        c = float(input("Please input the upper base of the trapezoid: "))
        break
    except ValueError:
        print("You have entered incorrect data, please try again use only numbers, for example 8, 8.54, 1000")

# of course, we can use standart encoding str in bytes,
# but pickle definetly more pleasant if we know that our server based on python3 too
data = (a, b, c)
data = pickle.dumps(data)

tcp_socket.connect(addr)
tcp_socket.sendall(data)
data = tcp_socket.recv(1024)
print("The area of the trapezoid is equal to:", pickle.loads(data))

tcp_socket.close()
