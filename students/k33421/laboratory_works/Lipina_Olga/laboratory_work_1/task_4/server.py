import threading
import socket

from typing import List

host ='localhost'
port = 8001
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients: List[socket.socket] = []
nicknames: List[bytes] = []


def broadcast(message: bytes):
    for client in clients:
        client.send(message)


def handle_client(client):
    """Getting client message and sending it to chat.
    In case of error (client disconnect) delete client from chat."""
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except: # any connection error or value error
            idx = clients.index(client)
            clients.remove(idx)
            broadcast(f"{nicknames[idx]} has left the chat.".encode())
            nicknames.remove(idx)
            client.close()
            break

def recieve_cons():
    while True:
        print("Server's listening...")
        client, address = server.accept()
        print(f"Connected with {address}")
        client.send("Send a nickname".encode())
        nickname = client.recv(1024)
        nicknames.append(nickname)
        clients.append(client)
        broadcast(f"{nickname} joined the chat.".encode())
        client.send("You are connected".encode())
        thread = threading.Thread(target=handle_client, args=(client, ))
        thread.start()

if __name__ == "__main__":
    recieve_cons()

