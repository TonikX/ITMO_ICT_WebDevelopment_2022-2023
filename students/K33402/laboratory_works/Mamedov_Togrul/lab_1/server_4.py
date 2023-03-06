import socket
import threading

host, port = "127.0.0.1", 2465
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
print(f"The chat at {host}:{port} was created")

clients = []


def send_to_everyone(message):
    for conn, name in clients:
        conn.send(f"{conn}: {message}")


def handle_message(client):
    while True:
        message = client.recv(8192)
        send_to_everyone(message)


def read_messages():
    message = "Whats your name?"
    while True:
        connection, address = server.accept()
        connection.sendto(message.encode("utf-8"), address)
        user = connection.recv(8192).decode("utf-8")
        clients.append((connection, user))
        thread = threading.Thread(target=handle_message, args=(connection,))
        thread.start()


if __name__ == '__main__':
    read_messages()