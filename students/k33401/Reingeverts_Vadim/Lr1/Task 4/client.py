import socket
from threading import Thread


name = input("Create a nickname: ") or "Anonymous"

# TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.1)

isConnected = True
try:
    sock.connect(('localhost', 12344))
except IOError:
    print("Could not connect to the server.")
    isConnected = False

while isConnected:
    try:
        text = input("Your message: ")
        message = f"{name}: {text}".encode("utf-8")
        sock.send(message)

        try:
            connection = sock.recv(2048)
            message = connection.decode('utf-8')
            print(message)
        # Handle timeout
        except IOError:
            print("???")
            continue
    except ConnectionResetError or ConnectionAbortedError:
        print("Server closed connection.")
    except ConnectionRefusedError:
        print("Could not connect to the server.")
    except KeyboardInterrupt:
        break


sock.close()
