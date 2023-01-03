import socket
import threading

def client_thread(client):
    while True:
        msg = client.recv(1024).decode('utf-8')
        broadcasting(msg, client)

def broadcasting(msg, client):
    for c in clients:
        if c != client:
            c.send(f"{clients[client]}: {msg}".encode('utf-8'))

clients = {}

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9095))
server.listen(5)

while True:
    client, address = server.accept()
    print(f"{address} joins chat")
    clients[client] = address
    threading.Thread(target=client_thread, args=(client,)).start()