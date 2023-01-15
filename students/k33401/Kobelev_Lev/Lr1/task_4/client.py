import socket, threading, os, time


def receive():
    try:
        while alive:
            message = sock.recv(1024).decode()
            if message == "NICKNAME":
                sock.send(nickname.encode())
            elif message == "END":
                print("\nThe chat is closed")
                os._exit(1)
            else:
                print(message)
    except KeyboardInterrupt:
        return


def write():
    try:
        while alive:
            message = "{}: {}".format(nickname, input(""))
            sock.send(message.encode())
    except KeyboardInterrupt:
        return


def kill_session():
    sock.send("EXIT".encode())
    sock.close()


def main():
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    write_thread = threading.Thread(target=write)
    write_thread.start()

    data = sock.recv(1024)
    print(data.decode())

    while True:
        pass


if __name__ == "__main__":
    alive = True
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    sock.connect(("localhost", 9094))

    nickname = input("Username: ")

    try:
        main()
    except KeyboardInterrupt:
        alive = False
        sock.send("EXIT".encode())
        print("\nYou left!")
        os._exit(1)
