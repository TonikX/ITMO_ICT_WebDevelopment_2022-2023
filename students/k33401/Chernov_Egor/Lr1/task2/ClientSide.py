import socket

sock = socket.socket()
sock.connect(("127.0.0.1", 8080))
massage = input("Which formula do you prefer?\na. S = a*h\nb. S = a*b*sin(a^b)\n"
                "c. S = 0.5*d1*d2+sin(d1^d2)\nInput latter and params: ")
sock.send(massage.encode("utf-8"))
sock.settimeout(1)
data = sock.recv(16384)
decodeData = data.decode("utf-8")
print("Answer: " + decodeData)
