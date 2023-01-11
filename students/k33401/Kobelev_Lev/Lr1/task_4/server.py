import socket, threading, os


class Client:
    def __init__(self, connection, username):
        self.connection = connection
        self.username = username


def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.connection.send(message)
            except socket.error:
                client.connection.close()
                clients.remove(client)


def handle(client):
    while True:
        message = client.connection.recv(1024)
        if message == b"EXIT":
            client.connection.close()
            clients.remove(client)
            broadcast("{} left!".format(client.username).encode(), client)
            break
        else:
            broadcast(message, client)


def main():
    while True:
        conn, addr = sock.accept()
        print("Connected with {}".format(str(addr)))

        conn.send("NICKNAME".encode())

        clients.append(Client(conn, conn.recv(1024).decode()))
        broadcast("{} joined!".format(clients[-1].username).encode(), conn)
        thread = threading.Thread(target=handle, args=(clients[-1],))
        thread.start()


if __name__ == "__main__":
    clients = []

    sock = socket.socket()
    sock.bind(("localhost", 9094))
    sock.listen(5)

    try:
        main()
    except KeyboardInterrupt:
        broadcast(b"END", sock)
        os._exit(1)
