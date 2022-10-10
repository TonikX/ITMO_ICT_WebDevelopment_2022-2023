import socket

def client():
    socketVar = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketVar.connect(('127.0.0.1', 1337))

    massage = input("Which formula do you prefer?\n"
                "a is Piffagor theorem\n"
                "b is Parallelogram Area\n"
                "c is Trapezoid Area)\n"
                "Input latter and params: ")
    socketVar.send(massage.encode("utf-8"))
    socketVar.settimeout(1)
    data = socketVar.recv(16384)
    decData = data.decode("utf-8")
    print("Result: " + decData)

